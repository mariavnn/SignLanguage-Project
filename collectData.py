import os
import cv2

DATA_DIR = './data'
number_of_classes = 3
dataset_size = 100

# Crear directorio de datos si no existe
os.makedirs(DATA_DIR, exist_ok=True)

# Iniciar captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Iterar sobre cada clase
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    os.makedirs(class_dir, exist_ok=True)
    print(f'Recopilando datos para la clase {j}')

    # Esperar a que el usuario esté listo para capturar
    input('Presiona Enter para comenzar a capturar...')

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "ENTER" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == 13:
            break
        
    
    # Capturar y guardar imágenes
    for i in range(dataset_size):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, f'{i}.jpg'), frame)

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
