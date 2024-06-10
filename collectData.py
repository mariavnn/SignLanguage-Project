# import os
# import cv2

# DATA_DIR = './data'
# PROGRESS_FILE = './progress.txt'

# if not os.path.exists(DATA_DIR):
#     os.makedirs(DATA_DIR)

# # Número de clases para el abecedario
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# number_of_classes = len(alphabet)
# dataset_size = 100

# # Leer el progreso actual desde el archivo
# def read_progress():
#     if os.path.exists(PROGRESS_FILE):
#         with open(PROGRESS_FILE, 'r') as file:
#             last_letter = file.read().strip()
#             if last_letter in alphabet:
#                 return alphabet.index(last_letter)
#     return 0

# # Guardar el progreso actual en el archivo
# def save_progress(letter):
#     with open(PROGRESS_FILE, 'w') as file:
#         file.write(letter)

# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Error: No se pudo abrir la cámara.")
#     exit()

# start_index = read_progress()

# for j in range(start_index, number_of_classes):
#     class_dir = os.path.join(DATA_DIR, alphabet[j])
#     if not os.path.exists(class_dir):
#         os.makedirs(class_dir)

#     print('Collecting data for letter {}'.format(alphabet[j]))

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: No se pudo leer el frame de la cámara.")
#             break
        
#         cv2.putText(frame, f'Ready to capture {alphabet[j]}? Press "Q" to start capturing!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(25) == ord('q'):
#             break

#     counter = 0
#     while counter < dataset_size:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: No se pudo leer el frame de la cámara.")
#             break
        
        
#         cv2.imshow('frame', frame)
#         key = cv2.waitKey(25)
#         if key == ord('q'):
#             save_progress(alphabet[j])  # Guardar progreso actual antes de salir
#             print(f'Paused. Progress saved at letter {alphabet[j]}.')
#             cap.release()
#             cv2.destroyAllWindows()
#             exit()
#         cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
#         counter += 1

#     # Guardar progreso después de completar la captura de la letra actual
#     save_progress(alphabet[j])

#     # Confirmar para proceder a la siguiente letra
#     print(f'Data collection for letter {alphabet[j]} completed. Press "N" to proceed to the next letter, or "S" to stop.')
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: No se pudo leer el frame de la cámara.")
#             break
        
#         cv2.putText(frame, f'Completed {alphabet[j]}! Press "N" to proceed to the next letter, or "S" to stop.', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
#         cv2.imshow('frame', frame)
#         key = cv2.waitKey(25)  # Esperar por la tecla, revisar cada 25 ms
#         if key == ord('n'):
#             break
#         elif key == ord('s'):
#             save_progress(alphabet[j])
#             print(f'Progress saved at letter {alphabet[j]}.')
#             cap.release()
#             cv2.destroyAllWindows()
#             exit()

# cap.release()
# cv2.destroyAllWindows()


import os
import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()