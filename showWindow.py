from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os, sys
from ui.showWindowUI import Ui_ShowWindow
import pyautogui
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from itemWidget import ItemWidget


class ShowWindow(QtWidgets.QMainWindow):
    def __init__(self, queue, photo, state, current_clothes):
        super(ShowWindow, self).__init__()

        self.currentimg = 0
        self.ui = Ui_ShowWindow()
        self.ui.setupUi(self)
        self.photo = photo
        self.init_UI()
        self.ui.label.setScaledContents(True)

        self.queue = queue
        self.state = state
        self.current_clothes = current_clothes

    def init_UI(self):
        self.display_width = 1920
        self.display_height = 1080
        self.setWindowTitle('Показ фото')
        self.ui.back_pushButton.clicked.connect(self.open_camera)
        self.ui.card_pushButton.clicked.connect(self.open_card)
        self.ui.to_card_pushButton.clicked.connect(self.to_card)
        self.ui.label.setPixmap(self.photo)

    def to_card(self):
        self.state['card'].append(self.current_clothes)

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
        print("clicked to open camera window")
        self.cameraWindow = CameraWindow(self.queue, self.state)
        self.cameraWindow.show()
        self.close()

    def open_card(self):
        from cardWindow import CardWindow
        self.cardWindow = CardWindow(self.queue, self.state)
        self.cardWindow.show()
        self.close()

    def closeEvent(self, event):
        event.accept()