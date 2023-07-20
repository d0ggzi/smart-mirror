from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal

from ui.cardItemWidgetUI import Ui_cardItem


class CardItemWidget(QWidget):
    def __init__(self, img, name, price, parent=None):
        super(CardItemWidget, self).__init__(parent)
        self.ui = Ui_cardItem()
        self.ui.setupUi(self)
        self.img = img
        self.name = name
        self.price = price

        self.init_ui()


    def init_ui(self):
        self.ui.photo_label.setPixmap(self.img)
        self.ui.photo_label.setScaledContents(True)
        self.ui.label.setText(self.name + "\n" + self.price + " рублей")
