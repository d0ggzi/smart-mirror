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
    def __init__(self, queue):
        super(CatalogWindow, self).__init__()

        self.currentimg = 0
        self.ui = Ui_CatalogWindow()
        self.ui.setupUi(self)

        self.init_UI()
        self.queue = queue

    def init_UI(self):
        self.display_width = 1920
        self.display_height = 1080
        self.setWindowTitle('Каталог')
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


    def open_camera(self):
        from cameraWindow import CameraWindow
        self.cameraWindow = CameraWindow(self.queue)
        self.cameraWindow.show()
        self.close()

    def open_card(self):
        from cardWindow import CardWindow
        self.cardWindow = CardWindow(self.queue)
        self.cardWindow.show()
        self.close()

    def closeEvent(self, event):
        event.accept()