from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os, sys
from ui.cardWindowUI import Ui_CardWindow
import pyautogui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from itemWidget import ItemWidget

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False


class CardWindow(QtWidgets.QMainWindow):
    def __init__(self, thread):
        super(CardWindow, self).__init__()

        self.currentimg = 0
        self.ui = Ui_CardWindow()
        self.ui.setupUi(self)
        self.previous_pressed = [0, 0, 0]
        self.times_for_pressed = 25
        self.init_UI()
        self.opened = True

        self.thread = thread
        self.thread.get_xy_signal.connect(self.get_x_y)
        self.thread.start()

    def init_UI(self):
        self.display_width = 1920
        self.display_height = 1080
        self.setWindowTitle('Корзина')
        self.buttons = [
            (520, 10, 81, 81, self.open_camera),
            (620, 10, 81, 81, self.open_gallery),
        ]
        self.ui.gallery_pushButton_2.clicked.connect(self.open_gallery)
        self.ui.fit_pushButton_2.clicked.connect(self.open_camera)
        # self.init_card_items()

    # def init_card_items(self):
    #     catalogdir = "img/catalog"
    #     catalogimg = [os.path.join(catalogdir, f) for f in os.listdir(catalogdir)]
    #     for index, img in enumerate(catalogimg):
    #         pixmap = QPixmap(img)
    #         item_widget = ItemWidget(pixmap, "Футболка", "990")
    #         self.ui.gridLayout_3.addWidget(item_widget, index//2, index%2)
    #         # if index == 1:
    #         #     break
            
            


    def get_x_y(self, coord_x, coord_y):
        if self.opened:
            coord_x = abs(coord_x - 640)
            coord_x *= self.display_width / 640 
            coord_y *= self.display_height / 480

            self.get_button_pressed(coord_x, coord_y)
            pyautogui.moveTo(coord_x, coord_y, duration=0.1)

    def get_button_pressed(self, coord_x, coord_y):
        if abs(self.previous_pressed[0] - coord_x) < 20 and abs(self.previous_pressed[1] - coord_y) < 20:
            self.previous_pressed[2] += 1
            if self.previous_pressed[2] % self.times_for_pressed == 0:
                pyautogui.click(coord_x, coord_y)
            self.previous_pressed = [coord_x, coord_y, self.previous_pressed[2]]
        else:
            self.previous_pressed = [coord_x, coord_y, 0]


    def open_camera(self):
        from cameraWindow import CameraWindow
        self.cameraWindow = CameraWindow(self.thread)
        self.cameraWindow.show()
        self.close()

    def open_gallery(self):
        from galleryWindow import GalleryWindow
        print("gallery pressed")
        self.catalog_window = GalleryWindow(self.thread)
        self.catalog_window.show()
        self.close()

    def closeEvent(self, event):
        self.opened = False
        self.thread.stop()
        event.accept()