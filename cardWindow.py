from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os, sys
from ui.cardWindowUI import Ui_CardWindow
import pyautogui
from cardItemWidget import CardItemWidget

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False


class CardWindow(QtWidgets.QMainWindow):
    def __init__(self, queue, state):
        super(CardWindow, self).__init__()
        self.state = state

        self.currentimg = 0
        self.ui = Ui_CardWindow()
        self.ui.setupUi(self)
        self.init_UI()

        self.queue = queue
        

    def init_UI(self):
        self.display_width = 1920
        self.display_height = 1080
        self.setWindowTitle('Корзина')
        self.ui.gallery_pushButton_2.clicked.connect(self.open_gallery)
        self.ui.fit_pushButton_2.clicked.connect(self.open_camera)
        self.init_card_items()

    def init_card_items(self):
        current_catalogimg = self.state['card']
        print(current_catalogimg)
        print(self.state)

        for index, img in enumerate(current_catalogimg):
            pixmap = QPixmap(img)
            text, price = img.split(os.sep)[-1].split('_')
            price = price.split('.')[0]
            item_widget = CardItemWidget(pixmap, text, price)
            self.ui.verticalLayout_3.addWidget(item_widget)

    def open_camera(self):
        from cameraWindow import CameraWindow
        self.cameraWindow = CameraWindow(self.queue, self.state)
        self.cameraWindow.show()
        self.close()

    def open_gallery(self):
        from galleryWindow import GalleryWindow
        print("gallery pressed")
        self.catalog_window = GalleryWindow(self.queue, self.state)
        self.catalog_window.show()
        self.close()

    def closeEvent(self, event):
        event.accept()