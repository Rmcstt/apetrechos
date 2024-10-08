import cv2
import os
import numpy as np

# Define os caracteres ASCII que serão usados para representar os pixels
ASCII_CHARS = "@%#*+=-:. asdfghjkl"

# Função para redimensionar a imagem para caber na tela do terminal


def resize_image(image, new_width=100):
    height, width = image.shape
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.60)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

# Função para converter a imagem para escala de cinza


def grayify(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Função para converter cada pixel em um caractere ASCII


def pixels_to_ascii(image):
    pixels = image.flatten()
    # Garante que o índice fique dentro do intervalo permitido para ASCII_CHARS
    ascii_str = "".join(
        [ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in pixels])
    return ascii_str

# Função principal para capturar vídeo e exibir em ASCII


def video_to_ascii():
    cap = cv2.VideoCapture(0)  # Inicia a captura de vídeo da câmera

    if not cap.isOpened():
        print("Não foi possível acessar a câmera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Falha ao capturar imagem")
            break

        # Reduz a imagem e converte para escala de cinza
        gray_image = grayify(frame)
        resized_gray_image = resize_image(gray_image)

        # Converte a imagem em uma string ASCII
        ascii_image = pixels_to_ascii(resized_gray_image)

        # Divide a string em linhas para exibir
        ascii_image_len = len(ascii_image)
        ascii_frame = "\n".join([ascii_image[i:(i + 100)]
                                for i in range(0, ascii_image_len, 100)])

        # Limpa a tela e imprime o quadro em ASCII
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_frame)

        # Aguarda 1 ms para o próximo quadro, saindo ao pressionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_to_ascii()
