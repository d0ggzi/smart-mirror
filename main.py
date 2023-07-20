from PyQt5 import QtWidgets
from cameraWindow import CameraWindow
from gestures import Gestures
from multiprocessing import Process, Queue


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    with Gestures() as gestures:
        queue = Queue()
        p = Process(target=gestures.run, args=(queue,))
        p.start()

        application = CameraWindow(queue, {'photo_taken': 0, 'card': []})
        application.show()
        
        if not app.exec():
            p.kill()
            exit()