from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
import os
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from ui.itemWidgetUI import Ui_catalogWidget


class ItemWidget(QWidget):
    to_card_signal = pyqtSignal(str)

    def __init__(self, img, parent=None):
        super(ItemWidget, self).__init__(parent)
        self.ui = Ui_catalogWidget()
        self.ui.setupUi(self)
        
        self.img = img
        self.img_show = QPixmap(img)
        try:
            self.name, price = img.split(os.sep)[-1].split('_')
            self.price = price.split('.')[0]
        except:
            self.name, self.price = 'Футболка', 990

        self.init_ui()


    def init_ui(self):
        self.ui.photo_label.setPixmap(self.img_show)
        self.ui.photo_label.setScaledContents(True)
        self.ui.card_pushButton.clicked.connect(self.to_card)
        self.ui.name_label.setText(self.name)
        self.ui.price_label.setText(str(self.price) + " рублей")

    def to_card(self):
        self.to_card_signal.emit(self.img)