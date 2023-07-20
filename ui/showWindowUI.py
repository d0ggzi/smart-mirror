# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowWindow(object):
    def setupUi(self, ShowWindow):
        ShowWindow.setObjectName("ShowWindow")
        ShowWindow.resize(720, 1100)
        self.centralwidget = QtWidgets.QWidget(ShowWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 6, 711, 1090))
        self.label.setText("")
        self.label.setObjectName("label")
        self.back_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.back_pushButton.setGeometry(QtCore.QRect(590, 40, 100, 100))
        self.back_pushButton.setStyleSheet("QPushButton { \n"
"background-color: rgb(0, 0, 0, 0.0);\n"
"border: 0px solid red;\n"
"}")
        self.back_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/UI-images/Кнопка выйти.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_pushButton.setIcon(icon)
        self.back_pushButton.setIconSize(QtCore.QSize(80, 80))
        self.back_pushButton.setObjectName("back_pushButton")
        self.card_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.card_pushButton.setGeometry(QtCore.QRect(10, 20, 130, 130))
        self.card_pushButton.setStyleSheet("QPushButton { \n"
"background-color: rgb(0, 0, 0, 0.0);\n"
"border: 0px solid red;\n"
"}")
        self.card_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/UI-images/card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_pushButton.setIcon(icon1)
        self.card_pushButton.setIconSize(QtCore.QSize(130, 130))
        self.card_pushButton.setObjectName("card_pushButton")
        self.to_card_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.to_card_pushButton.setGeometry(QtCore.QRect(270, 820, 200, 60))
        self.to_card_pushButton.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.to_card_pushButton.setFont(font)
        self.to_card_pushButton.setStyleSheet("color: black;\n"
"border: 3px solid black;\n"
"border-radius: 15px;")
        self.to_card_pushButton.setObjectName("to_card_pushButton")
        ShowWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ShowWindow)
        QtCore.QMetaObject.connectSlotsByName(ShowWindow)

    def retranslateUi(self, ShowWindow):
        _translate = QtCore.QCoreApplication.translate
        ShowWindow.setWindowTitle(_translate("ShowWindow", "MainWindow"))
        self.to_card_pushButton.setText(_translate("ShowWindow", "В корзину"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShowWindow = QtWidgets.QMainWindow()
    ui = Ui_ShowWindow()
    ui.setupUi(ShowWindow)
    ShowWindow.show()
    sys.exit(app.exec_())
