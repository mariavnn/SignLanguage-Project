import os
import cv2

DATA_DIR = './data'
number_of_classes = 26
dataset_size = 100

# Lista de letras del alfabeto
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Crear directorio de datos si no existe
os.makedirs(DATA_DIR, exist_ok=True)

# Iniciar captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Iterar sobre cada clase
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, alphabet[j])  # Usar la letra del alfabeto como nombre de directorio
    os.makedirs(class_dir, exist_ok=True)
    print(f'Recopilando datos para la letra {alphabet[j]}')

    # Esperar a que el usuario esté listo para capturar
    input(f'Presiona Enter para comenzar a grabar la letra {alphabet[j]}...')

    # Bucle para capturar las imágenes
    for i in range(dataset_size):
        print(f'Grabando data de la letra {alphabet[j]} ({i+1}/{dataset_size})')
        
        ret, frame = cap.read()
        cv2.putText(frame, f'Recording letter {alphabet[j]}', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, f'{i}.jpg'), frame)

    # Pausa antes de continuar con la siguiente letra
    input('Presiona Enter para continuar con la siguiente letra...')

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
