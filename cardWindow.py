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
    def __init__(self, queue):
        super(CardWindow, self).__init__()

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
            
            


    def open_camera(self):
        from cameraWindow import CameraWindow
        self.cameraWindow = CameraWindow(self.queue)
        self.cameraWindow.show()
        self.close()

    def open_gallery(self):
        from galleryWindow import GalleryWindow
        print("gallery pressed")
        self.catalog_window = GalleryWindow(self.queue)
        self.catalog_window.show()
        self.close()

    def closeEvent(self, event):
        event.accept()