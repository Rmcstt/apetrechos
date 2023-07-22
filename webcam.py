import cv2
import numpy as np
from Quartz import CoreGraphics

def get_webcam_image():
    # Ajusta a largura e altura da imagem da webcam (opcional)
    width, height = 640, 480

    # Cria um contexto da captura da webcam
    capture = cv2.VideoCapture(0)

    # Define o tamanho da imagem da captura da webcam
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Captura a imagem da webcam
    ret, frame = capture.read()

    # Encerra a captura da webcam
    capture.release()

    if not ret:
        print("Não foi possível capturar a foto da webcam.")
        return None

    return frame

def save_webcam_photo(image):
    # Salva a imagem em um arquivo
    cv2.imwrite("webcam_photo.jpg", image)
    print("Foto da webcam salva com sucesso!")

def show_webcam_photo(image):
    # Mostra a imagem capturada em uma janela
    cv2.imshow("Webcam Photo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    webcam_image = get_webcam_image()

    if webcam_image is not None:
        show_webcam_photo(webcam_image)
        save_webcam_photo(webcam_image)
