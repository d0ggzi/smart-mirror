import cv2
import mediapipe as mp
import time
import numpy as np
from PyQt5.QtCore import pyqtSignal, QThread
from tensorflow.keras.models import load_model


class Gestures(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    get_xy_signal = pyqtSignal(int, int)
    get_gesture_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.n_poses = 10
        self.was_predicted = False
        self.recognition_time = time.time()
        self.previous_gesture = {
            'gesture': "",
            'repeated': 0,
        }

        self.model = load_model('mp_hand_gesture')
        with open('gesture.names', 'r') as f:
            self.classNames = f.read().split('\n')

        self.cap = cv2.VideoCapture(0)

    def run(self):
        with self.mp_hands.Hands(
                max_num_hands=1,
                model_complexity=0,
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
                    # for hand_landmarks in self.results:
                    #     self.mp_drawing.draw_landmarks(
                    #         image,
                    #         hand_landmarks,
                    #         self.mp_hands.HAND_CONNECTIONS,
                    #         self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    #         self.mp_drawing_styles.get_default_hand_connections_style())
                    if self.was_predicted:
                        prediction = self.model.predict([landmarks], verbose = 0)
                        classID = np.argmax(prediction)
                        className = self.classNames[classID]
                        self.get_gesture(className)
                    self.was_predicted = not self.was_predicted
                self.change_pixmap_signal.emit(cv2.flip(image, 1))
                self.get_xy_signal.emit(cx, cy)
        self.cap.release()

    def get_gesture(self, gesture):
        if self.previous_gesture['gesture'] == gesture:
            self.previous_gesture['repeated'] += 1
            if self.previous_gesture['repeated'] == 10:
                self.get_gesture_signal.emit(gesture)
        else:
            self.previous_gesture['gesture'] = gesture
            self.previous_gesture['repeated'] = 1
    
    def stop(self):
        pass
