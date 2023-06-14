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


class CameraWindow(QtWidgets.QMainWindow):
    def __init__(self, queue):
        super(CameraWindow, self).__init__()

        self.currentimg = 3
        self.photo_taken = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

        self.timer = QTimer()
        self.opened = True
        self.queue = queue
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
        self.ui.label_8.setText(str(self.photo_taken))

        self.ui.galleryButton.clicked.connect(self.gallery)
        # self.ui.card_pushButton.clicked.connect(self.add_to_card)
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



    # def get_x_y(self, coord_x, coord_y):
    #     if self.opened:
    #         coord_x = abs(coord_x - 640)
    #         coord_x *= self.display_width / 640 
    #         coord_y *= self.display_height / 480

    #         button = self.get_button_pressed(coord_x, coord_y)
    #         if button is not None:
    #             self.button_pressed['name'] = button
    #             self.button_pressed['times'] += 1
    #             if self.button_pressed['times'] % self.times_for_pressed == 0:
    #                 button[4]()
    #         else:
    #             self.button_pressed = {
    #                 "name": "",
    #                 "times": 0,
    #             }

    def get_gesture(self, gesture):
        if gesture == "peace":
            self.take_photo()
        print(gesture)


    def update_image(self):
        """Updates the image_label with a new opencv image"""
        try:
            while not self.queue.empty():
                cv_img = self.queue.get_nowait()
                self.cv_img  = cv2.rotate(cv_img, cv2.ROTATE_90_CLOCKWISE)
                qt_img = self.convert_cv_qt()
                self.ui.camera_label.setPixmap(qt_img)

                self.ui.time_label.setText(str(abs(round(self.timer.remainingTime()/1000, 1))))
        except:
            pass


    def convert_cv_qt(self):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    
    def save_photo(self):
        cv_img_rgb = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(cv_img_rgb)
        
        img_name = datetime.now().strftime("img_%d-%m_%H-%M-%S.jpg")
        im_pil.save(f'img/gallery/{img_name}')

        self.timer.stop()
        self.photo_taken += 1
        self.ui.label_8.setText(str(self.photo_taken))

    def get_button_pressed(self, coord_x, coord_y):
        for rect in self.buttons:
            x1, y1, w, h, name = rect
            x2, y2 = x1+w, y1+h
            x, y = coord_x, coord_y
            if (x1 < x and x < x2):
                if (y1 < y and y < y2):
                    return rect
        return None

    def back(self):
        print("back pressed")

    def right(self):
        print("right pressed")
        self.currentimg += 1
        self.init_images()

    def left(self):
        print("left pressed")
        self.currentimg -= 1
        self.init_images()

    def take_photo(self):
        if self.timer.remainingTime() == -1:
            self.timer = QTimer()
            self.timer.setInterval(5000)
            self.timer.timeout.connect(self.save_photo)
            self.timer.start()
            # self.do_AI_things()
            # self.show_photo()

    def catalog(self):
        from catalogWindow import CatalogWindow
        print("catalog pressed")
        self.catalog_window = CatalogWindow(self.queue)
        self.catalog_window.show()
        self.close()

    def gallery(self):
        from galleryWindow import GalleryWindow
        print("gallery pressed")
        self.catalog_window = GalleryWindow(self.queue)
        self.catalog_window.show()
        self.close()

    def closeEvent(self, event):
        event.accept()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CameraWindow()
    application.show()
    
    sys.exit(app.exec())