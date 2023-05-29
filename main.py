from PyQt5 import QtWidgets
import sys
from cameraWindow import CameraWindow
from gestures import Gestures


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    gestures = Gestures()
    application = CameraWindow(gestures)
    application.show()
    
    sys.exit(app.exec())