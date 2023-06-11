# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smart-mirror-vert.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1150)
        MainWindow.setMinimumSize(QtCore.QSize(150, 150))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 202, 1138))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(150, 150))
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 150))
        self.label_2.setMaximumSize(QtCore.QSize(150, 150))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(150, 150))
        self.label_3.setMaximumSize(QtCore.QSize(150, 150))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 200))
        self.label_4.setMaximumSize(QtCore.QSize(200, 200))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(150, 150))
        self.label_5.setMaximumSize(QtCore.QSize(150, 150))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(150, 150))
        self.label_6.setMaximumSize(QtCore.QSize(150, 150))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(150, 150))
        self.label_7.setMaximumSize(QtCore.QSize(150, 150))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.takePhotoButton = QtWidgets.QPushButton(self.centralwidget)
        self.takePhotoButton.setGeometry(QtCore.QRect(320, 840, 181, 161))
        self.takePhotoButton.setStyleSheet("QPushButton { \n"
"background-color: rgb(0, 0, 0, 0.0);\n"
"border: 0px solid red;\n"
"}")
        self.takePhotoButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/UI-images/Кнопка фото.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.takePhotoButton.setIcon(icon)
        self.takePhotoButton.setIconSize(QtCore.QSize(200, 200))
        self.takePhotoButton.setObjectName("takePhotoButton")
        self.rightButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightButton.setGeometry(QtCore.QRect(670, 620, 81, 141))
        self.rightButton.setStyleSheet("QPushButton { \n"
"background-color: rgb(0, 0, 0, 0.0);\n"
"border: 0px solid red;\n"
"}")
        self.rightButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/UI-images/Кнопка вниз.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightButton.setIcon(icon1)
        self.rightButton.setIconSize(QtCore.QSize(180, 180))
        self.rightButton.setObjectName("rightButton")
        self.leftButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftButton.setGeometry(QtCore.QRect(670, 430, 81, 141))
        self.leftButton.setStyleSheet("QPushButton { \n"
"background-color: rgb(0, 0, 0, 0.0);\n"
"border: 0px solid red;\n"
"}")
        self.leftButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/UI-images/Кнопка вверх.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftButton.setIcon(icon2)
        self.leftButton.setIconSize(QtCore.QSize(180, 180))
        self.leftButton.setObjectName("leftButton")
        self.catalogButton = QtWidgets.QPushButton(self.centralwidget)
        self.catalogButton.setGeometry(QtCore.QRect(660, 850, 100, 100))
        self.catalogButton.setStyleSheet("QPushButton { \n"
"background-color: rgb(0, 0, 0, 0.0);\n"
"border: 0px solid red;\n"
"}")
        self.catalogButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/UI-images/Кнопка в каталог.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.catalogButton.setIcon(icon3)
        self.catalogButton.setIconSize(QtCore.QSize(100, 100))
        self.catalogButton.setObjectName("catalogButton")
        self.galleryButton = QtWidgets.QPushButton(self.centralwidget)
        self.galleryButton.setGeometry(QtCore.QRect(660, 270, 100, 100))
        self.galleryButton.setStyleSheet("QPushButton { \n"
"background-color: rgb(0, 0, 0, 0.0);\n"
"border: 0px solid red;\n"
"}")
        self.galleryButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/UI-images/Кнопка в галерею.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.galleryButton.setIcon(icon4)
        self.galleryButton.setIconSize(QtCore.QSize(100, 100))
        self.galleryButton.setObjectName("galleryButton")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(290, 70, 161, 100))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: black;")
        self.time_label.setText("")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(600, 70, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: black;")
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.card_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.card_pushButton.setGeometry(QtCore.QRect(310, 1010, 200, 60))
        self.card_pushButton.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.card_pushButton.setFont(font)
        self.card_pushButton.setStyleSheet("color: black;\n"
"border: 3px solid black;\n"
"border-radius: 15px;")
        self.card_pushButton.setObjectName("card_pushButton")
        self.camera_label = QtWidgets.QLabel(self.centralwidget)
        self.camera_label.setGeometry(QtCore.QRect(0, 0, 800, 1150))
        self.camera_label.setMinimumSize(QtCore.QSize(800, 1150))
        self.camera_label.setMaximumSize(QtCore.QSize(800, 1150))
        self.camera_label.setText("")
        self.camera_label.setObjectName("camera_label")
        self.camera_label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.takePhotoButton.raise_()
        self.rightButton.raise_()
        self.leftButton.raise_()
        self.catalogButton.raise_()
        self.galleryButton.raise_()
        self.time_label.raise_()
        self.label_8.raise_()
        self.card_pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.card_pushButton.setText(_translate("MainWindow", "В корзину"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
