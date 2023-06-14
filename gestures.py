import cv2
import mediapipe as mp
import numpy as np
import os
import atexit
import pyautogui
from tensorflow.keras.models import load_model

pyautogui.PAUSE = 0
pyautogui.MINIMUM_SLEEP = 0


class Gestures():
    def __enter__(self):
        return self

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.n_poses = 10
        self.was_predicted = False
        self.previous_gesture = {
            'gesture': "",
            'repeated': 0,
        }
        self.previous_pressed = [0, 0, 0]
        self.times_for_pressed = 25
        self.display_width = 1920
        self.display_height = 1080

        self.model = load_model('mp_hand_gesture')
        with open('gesture.names', 'r') as f:
            self.classNames = f.read().split('\n')

        self.cap = cv2.VideoCapture(0)
        atexit.register(self.stop)

    def run(self, queue):
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
                    # if self.was_predicted:
                    #     prediction = self.model.predict([landmarks], verbose = 0)
                    #     classID = np.argmax(prediction)
                    #     className = self.classNames[classID]
                    #     # self.get_gesture(className)
                    # self.was_predicted = not self.was_predicted
                # self.change_pixmap_signal.emit(cv2.flip(image, 1))
                    cx = abs(cx - 640)
                    cx *= self.display_width / 640 
                    cy *= self.display_height / 480

                    self.get_button_pressed(cx, cy)
                    pyautogui.moveTo(cx, cy, duration=0.1)
                queue.put(cv2.flip(image, 1), block=False)
                    
                # self.get_xy_signal.emit(cx, cy)
        self.cap.release()

    # def get_gesture(self, gesture):
    #     if self.previous_gesture['gesture'] == gesture:
    #         self.previous_gesture['repeated'] += 1
    #         if self.previous_gesture['repeated'] == 10:
    #             self.get_gesture_signal.emit(gesture)
    #     else:
    #         self.previous_gesture['gesture'] = gesture
    #         self.previous_gesture['repeated'] = 1

    def get_button_pressed(self, coord_x, coord_y):
        if abs(self.previous_pressed[0] - coord_x) < 20 and abs(self.previous_pressed[1] - coord_y) < 20:
            self.previous_pressed[2] += 1
            if self.previous_pressed[2] % self.times_for_pressed == 0:
                pyautogui.click(coord_x, coord_y)
            self.previous_pressed = [coord_x, coord_y, self.previous_pressed[2]]
        else:
            self.previous_pressed = [coord_x, coord_y, 0]
    
    def stop(self):
        self.cap.release()

    def __exit__(self, exc_type, exc_value, traceback):
        self.cap.release()