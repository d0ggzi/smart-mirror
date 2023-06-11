import cv2
import mediapipe as mp
import time
import numpy as np
import atexit
from PyQt5.QtCore import pyqtSignal, QThread


class Gestures(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    get_xy_signal = pyqtSignal(int, int)
    get_gesture_signal = pyqtSignal(str)

    def __enter__(self):
        return self

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands

        self.cap = cv2.VideoCapture(self.gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
        atexit.register(self.stop)

    def gstreamer_pipeline(self,
     sensor_id=0,
     capture_width=1280,
     capture_height=960,
     display_width=640,
     display_height=480,
     framerate=30,
     flip_method=0,
 ):
     return (
  "nvarguscamerasrc sensor-id=%d ! "
  "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
  "nvvidconv flip-method=%d ! "
  "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
  "videoconvert ! "
  "video/x-raw, format=(string)BGR ! appsink"
  % (
      sensor_id,
      capture_width,
      capture_height,
      framerate,
      flip_method,
      display_width,
      display_height,
  )
     )

    def run(self):
        with self.mp_hands.Hands(
                max_num_hands=1,
                min_detection_confidence=0.7,
                min_tracking_confidence=0.7) as hands:
            while self.cap.isOpened() and self._run_flag:
                success, image = self.cap.read()
                if not success:
                    continue

                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                self.results = hands.process(image).multi_hand_landmarks

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                h, w, _ = image.shape
                cx, cy = 0, 0
                landmarks = []
                if self.results:
                    for hand_landmarks in self.results:
                        for handslm in hand_landmarks.landmark:
                            xh = int(handslm.x * h)
                            yh = int(handslm.y * w)
                            landmarks.append([xh, yh])
                    cx, cy = int(self.results[0].landmark[8].x * w), int(self.results[0].landmark[8].y * h)
                    cv2.circle(image, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                self.change_pixmap_signal.emit(cv2.flip(image, 1))
                self.get_xy_signal.emit(cx, cy)
        self.cap.release()
    
    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def __exit__(self, exc_type, exc_value, traceback):
        self.cap.release()
        cv2.destroyAllWindows()