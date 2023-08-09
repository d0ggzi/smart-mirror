from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import cv2
import os
from PyQt5.QtCore import pyqtSlot, Qt, QTimer
import numpy as np
from ui.mainWindowUI import Ui_MainWindow
from PIL import Image
from datetime import datetime
from cvfpscalc import CvFpsCalc
from multiprocessing.pool import ThreadPool
from PIL import Image
from size_recognizer.SizeRecognozer import SizeRecognizer


class CameraWindow(QtWidgets.QMainWindow):
    def __init__(self, queue, state):
        super(CameraWindow, self).__init__()
        self.state = state
        self.current_clothes = ''

        self.currentimg = 3
        # self.cvfpscalc = CvFpsCalc(buffer_len=10)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

        self.timer = QTimer()
        self.queue = queue
        self.size_recognizer = SizeRecognizer()
        self.img_to_show = None
        
        self.ui.camera_label.setScaledContents(True)
        # connect its signal to the update_image slot
        # start the thread
        self.timer2 = QTimer()
        self.timer2.setInterval(30)
        self.timer2.timeout.connect(self.update_image)
        self.timer2.start()
    
    def init_UI(self):
        self.display_width = 1280
        self.display_height = 960
        self.setWindowTitle('Умное зеркало')
        self.init_images()
        self.ui.label_8.setText(str(self.state['photo_taken']))

        self.ui.galleryButton.clicked.connect(self.gallery)
        self.ui.card_pushButton.clicked.connect(self.add_to_card)
        self.ui.catalogButton.clicked.connect(self.catalog)
        self.ui.rightButton.clicked.connect(self.right)
        self.ui.leftButton.clicked.connect(self.left)
        self.ui.takePhotoButton.clicked.connect(self.take_photo)

    def init_images(self, filter=None):
        catalogmaindir = "img/catalog"
        self.labels = [self.ui.label, self.ui.label_2, self.ui.label_3, self.ui.label_4, self.ui.label_5, self.ui.label_6, self.ui.label_7]
        catalogdirs = [os.path.join(catalogmaindir, f) for f in os.listdir(catalogmaindir)]
        catalogimg = dict()
        for catalogdir in catalogdirs:
            catalogimg[catalogdir.split(os.sep)[-1]] = [os.path.join(catalogdir, f) for f in os.listdir(catalogdir)]

        current_catalogimg = [None, None, None]
        if filter is not None: current_catalogimg += catalogimg[filter]
        else:
            for el in catalogimg.keys():
                current_catalogimg += catalogimg[el]
        current_catalogimg += [None, None, None]


        if self.currentimg < 0: self.currentimg = 0
        elif self.currentimg > len(current_catalogimg) - 7: self.currentimg -= 1
        for index in range(self.currentimg, self.currentimg + 7):
            current_label = self.labels[index - self.currentimg]
            if current_catalogimg[index] is not None:
                pixmap = QPixmap(current_catalogimg[index])
                current_label.setPixmap(pixmap)
                current_label.setScaledContents(True)
            else:
                current_label.clear()
        self.current_clothes = current_catalogimg[self.currentimg + 3]

    # def get_gesture(self, gesture):
    #     if gesture == "peace":
    #         self.take_photo()


    def update_image(self):
        """Updates the image_label with a new opencv image"""
        try:
            while not self.queue.empty():
                cv_img = self.queue.get_nowait()
                self.cv_img  = cv2.rotate(cv_img, cv2.ROTATE_90_CLOCKWISE)
                self.qt_img = self.convert_cv_qt(self.cv_img)
                self.ui.camera_label.setPixmap(self.qt_img)
                # print(self.cvfpscalc.get())

                self.ui.time_label.setText(str(abs(round(self.timer.remainingTime()/1000, 1))))

                if self.img_to_show is not None:
                    self.show_photo()
        except:
            pass


    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
    def save_photo(self):
        cv_img_rgb = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(cv_img_rgb)
        
        img_name = datetime.now().strftime(f"%d-%m_%H-%M-%S&{self.current_clothes.split('.')[0].replace(os.sep, '#')}.jpg")
        im_pil.save(f'img/gallery/{img_name}')

        self.timer.stop()
        self.state['photo_taken'] += 1
        self.ui.label_8.setText(str(self.state['photo_taken']))

        # self.do_AI_things()
        pool = ThreadPool(processes=1)
        async_result = pool.apply_async(self.recognize_photo, ())
    

    def add_to_card(self):
        self.state['card'].append(self.current_clothes)
        # print(self.state)


    def back(self):
        print("back pressed")

    def right(self):
        # print("right pressed")
        self.currentimg += 1
        self.init_images()

    def left(self):
        # print("left pressed")
        self.currentimg -= 1
        self.init_images()

    def take_photo(self):
        if self.timer.remainingTime() == -1:
            self.timer = QTimer()
            self.timer.setInterval(5000)
            self.timer.timeout.connect(self.save_photo)
            self.timer.start()
            

    def show_photo(self):
        from showWindow import ShowWindow
        # print("showing photo")

        self.show_window = ShowWindow(self.queue, self.img_to_show, self.state, self.current_clothes)
        self.show_window.show()
        self.img_to_show = None
        self.close()

    def recognize_photo(self):
        pil_img = Image.fromarray(self.cv_img)
        image = self.size_recognizer.get_image_with_size(pil_img)
        self.img_to_show = self.convert_cv_qt(image)

    def catalog(self):
        from catalogWindow import CatalogWindow
        # print("catalog pressed")
        self.catalog_window = CatalogWindow(self.queue, self.state)
        self.catalog_window.show()
        self.close()

    def gallery(self):
        from galleryWindow import GalleryWindow
        # print("gallery pressed")
        self.catalog_window = GalleryWindow(self.queue, self.state)
        self.catalog_window.show()
        self.close()

    def closeEvent(self, event):
        event.accept()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CameraWindow()
    application.show()
    
    sys.exit(app.exec())