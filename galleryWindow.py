from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os, sys
from ui.galleryWindowUI import Ui_GalleryWindow
import pyautogui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from itemWidget import ItemWidget

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False


class GalleryWindow(QtWidgets.QMainWindow):
    def __init__(self, queue):
        super(GalleryWindow, self).__init__()

        self.currentimg = 0
        self.ui = Ui_GalleryWindow()
        self.ui.setupUi(self)
        self.init_UI()
        
        self.queue = queue

    def init_UI(self):
        self.display_width = 1920
        self.display_height = 1080
        self.setWindowTitle('Галерея')
        self.buttons = [
            (520, 10, 81, 81, self.open_camera),
            (620, 10, 81, 81, self.open_card),
        ]
        self.ui.card_pushButton.clicked.connect(self.open_card)
        self.ui.fit_pushButton.clicked.connect(self.open_camera)
        self.init_Gallery_items()

    def init_Gallery_items(self):
        Gallerydir = "img/gallery"
        Galleryimg = [os.path.join(Gallerydir, f) for f in os.listdir(Gallerydir)]
        for index, img in enumerate(Galleryimg):
            pixmap = QPixmap(img)
            item_widget = ItemWidget(pixmap, "Футболка", "990")
            self.ui.gridLayout_3.addWidget(item_widget, index//2, index%2)
            # if index == 1:
            #     break
            
            

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