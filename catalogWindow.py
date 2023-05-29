from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os, sys
from ui.catalogWindowUI import Ui_CatalogWindow
import pyautogui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from itemWidget import ItemWidget

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False


class CatalogWindow(QtWidgets.QMainWindow):
    def __init__(self, thread):
        super(CatalogWindow, self).__init__()

        self.currentimg = 0
        self.ui = Ui_CatalogWindow()
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
        self.setWindowTitle('Каталог')
        self.buttons = [
            (520, 10, 81, 81, self.open_camera),
            (620, 10, 81, 81, self.open_card),
        ]
        self.ui.card_pushButton.clicked.connect(self.open_card)
        self.ui.fit_pushButton.clicked.connect(self.open_camera)
        self.init_catalog_items()

    def init_catalog_items(self, filter=None):
        catalogmaindir = "img/catalog"
        catalogdirs = [os.path.join(catalogmaindir, f) for f in os.listdir(catalogmaindir)]
        catalogimg = dict()
        for catalogdir in catalogdirs:
            catalogimg[catalogdir.split(os.sep)[-1]] = [os.path.join(catalogdir, f) for f in os.listdir(catalogdir)]

        current_catalogimg = []
        if filter is not None: current_catalogimg += catalogimg[filter]
        else:
            for el in catalogimg.keys():
                current_catalogimg += catalogimg[el]

        for index, img in enumerate(current_catalogimg):
            pixmap = QPixmap(img)
            text, price = img.split(os.sep)[-1].split('_')
            price = price.split('.')[0]
            item_widget = ItemWidget(pixmap, text, price)
            self.ui.gridLayout_3.addWidget(item_widget, index//2, index%2)


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

    def open_card(self):
        from cardWindow import CardWindow
        self.cardWindow = CardWindow(self.thread)
        self.cardWindow.show()
        self.close()

    def closeEvent(self, event):
        self.opened = False
        self.thread.stop()
        event.accept()