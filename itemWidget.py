from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal

from ui.itemWidgetUI import Ui_catalogWidget


class ItemWidget(QWidget):
    def __init__(self, img, name, price, parent=None):
        super(ItemWidget, self).__init__(parent)
        self.ui = Ui_catalogWidget()
        self.ui.setupUi(self)
        self.img = img
        self.name = name
        self.price = price

        self.init_ui()


    def init_ui(self):
        self.ui.photo_label.setPixmap(self.img)
        self.ui.photo_label.setScaledContents(True)
        self.ui.card_pushButton.clicked.connect(self.to_card)
        self.ui.name_label.setText(self.name)
        self.ui.price_label.setText(self.price + " рублей")

    def to_card(self):
        pass