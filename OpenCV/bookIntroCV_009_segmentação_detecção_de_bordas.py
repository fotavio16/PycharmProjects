'''

  Livro-Introdução-a-Visão-Computacional-com-Python-e-OpenCV-3

Repositório de imagens
https://github.com/opencv/opencv/tree/master/samples/data
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
#import mahotas

VERMELHO = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL = (255, 0, 0)
AMARELO = (0, 255, 255)
BRANCO = (255,255,255)
CIANO = (255, 255, 0)
PRETO = (0, 0, 0)

img = cv2.imread('ponte2.jpg') # Flag 1 = Color, 0 = Gray, -1 = Unchanged
img = img[::2,::2] # Diminui a imagem

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Sobel
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)

resultado = np.vstack([
    np.hstack([img, sobelX]),
    np.hstack([sobelY, sobel])
    ])

cv2.imshow("Sobel", resultado)
cv2.waitKey(0)

#Filtro Laplaciano
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

resultado = np.vstack([img, lap])

cv2.imshow("Filtro Laplaciano", resultado)
cv2.waitKey(0)

#Detector de bordas Canny
suave = cv2.GaussianBlur(img, (7, 7), 0)
canny1 = cv2.Canny(suave, 20, 120)
canny2 = cv2.Canny(suave, 70, 200)

resultado = np.vstack([
    np.hstack([img, suave ]),
    np.hstack([canny1, canny2])
    ])

cv2.imshow("Detector de Bordas Canny", resultado)
cv2.waitKey(0)


