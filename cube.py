import math
import time
import os

A = B = C = 0
cubeWidth = 20
width, height = 160, 44
zBuffer = [0] * (width * height)
buffer = [' '] * (width * height)
backgroundASCIICode = '.'
distanceFromCam = 100
horizontalOffset = 0
K1 = 40
incrementSpeed = 0.9


def calculateX(i, j, k):
    return (j * math.sin(A) * math.sin(B) * math.cos(C) -
            k * math.cos(A) * math.sin(B) * math.cos(C) +
            j * math.cos(A) * math.sin(C) +
            k * math.sin(A) * math.sin(C) +
            i * math.cos(B) * math.cos(C))


def calculateY(i, j, k):
    return (j * math.cos(A) * math.cos(C) +
            k * math.sin(A) * math.cos(C) -
            j * math.sin(A) * math.sin(B) * math.sin(C) +
            k * math.cos(A) * math.sin(B) * math.sin(C) -
            i * math.cos(B) * math.sin(C))


def calculateZ(i, j, k):
    return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)


def calculateForSurface(cubeX, cubeY, cubeZ, ch):
    global buffer, zBuffer
    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1 / z if z != 0 else 0

    xp = int(width / 2 + horizontalOffset + K1 * ooz * x * 2)
    yp = int(height / 2 + K1 * ooz * y)

    idx = xp + yp * width
    if 0 <= idx < width * height:
        if ooz > zBuffer[idx]:
            zBuffer[idx] = ooz
            buffer[idx] = ch


def render_frame():
    global A, B, C, zBuffer, buffer
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        buffer = [' '] * (width * height)
        zBuffer = [0] * (width * height)

        cubeWidth = 20
        horizontalOffset = -2 * cubeWidth

        # Desenhando todas as 6 faces do cubo
        cubeX = -cubeWidth
        while cubeX < cubeWidth:
            cubeY = -cubeWidth
            while cubeY < cubeWidth:
                # Face frontal
                calculateForSurface(cubeX, cubeY, -cubeWidth, '@')
                # Face traseira
                calculateForSurface(cubeX, cubeY, cubeWidth, '#')
                # Face esquerda
                calculateForSurface(-cubeWidth, cubeY, cubeX, '$')
                # Face direita
                calculateForSurface(cubeWidth, cubeY, cubeX, '%')
                # Face inferior
                calculateForSurface(cubeX, -cubeWidth, cubeY, ';')
                # Face superior
                calculateForSurface(cubeX, cubeWidth, cubeY, '+')
                cubeY += incrementSpeed
            cubeX += incrementSpeed

        # Impressão da tela
        for k in range(width * height):
            print(buffer[k] if k % width else '\n', end='')

        # Incrementos de rotação
        A += 0.05
        B += 0.05
        C += 0.01
        time.sleep(0.016)  # Aproximadamente 60fps


if __name__ == '__main__':
    render_frame()
