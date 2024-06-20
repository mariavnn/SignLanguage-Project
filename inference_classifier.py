import cv2
import mediapipe as mp
import pickle
import numpy as np

import warnings
warnings.filterwarnings("ignore", category=UserWarning, message='SymbolDatabase.GetPrototype() is deprecated.')


model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
labels_dict = {0: 'A', 1:'B', 2: 'C', 3: 'D', 4: 'E', 5:'F', 6: 'i', 7: 'K',
               8: 'L', 9: 'O', 10: 'Q', 11: 'R', 12:'T', 13: 'U', 14: 'V', 15: 'W',
               16: 'X', 17: 'Y', 18: 'Triste', 19: 'Hospital', 20: 'Profesor', 21: 'Silencio',
               22: 'Bien', 23: 'Mal', 24: 'Siete', 25: 'Seis', 26: 'Ocho'
               }

while True:
    data_aux = []
    x_ = []
    y_ = []
    ret, frame = cap.read()
    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, 
                mp_hands.HAND_CONNECTIONS, 
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

        for hand_landmarks in result.multi_hand_landmarks:
               for i in range(len(hand_landmarks.landmark)):
                   x = hand_landmarks.landmark[i].x
                   y = hand_landmarks.landmark[i].y
                   data_aux.append(x)
                   data_aux.append(y)
                   x_.append(x)
                   y_.append(y)
        while len(data_aux) < 84:
            data_aux.append(0)
        
        x1 = int(min(x_) * W)
        y1 = int(min(y_) * H)

        x2 = int(min(x_) * W)
        y2 = int(min(y_) * H)

        prediction = model.predict([np.asarray(data_aux)])
        predicted_character = labels_dict[int(prediction[0])]

        print(predicted_character)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predicted_character, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(25)

cap.release()
cv2.destroyAllWindows()   