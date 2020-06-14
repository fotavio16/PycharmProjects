'''

  Livro-Introdução-a-Visão-Computacional-com-Python-e-OpenCV-3

Repositório de imagens
https://github.com/opencv/opencv/tree/master/samples/data
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

VERMELHO = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL = (255, 0, 0)
AMARELO = (0, 255, 255)
BRANCO = (255,255,255)
CIANO = (255, 255, 0)
PRETO = (0, 0, 0)

img = cv2.imread('ponte2.jpg') # Flag 1 = Color, 0 = Gray, -1 = Unchanged
#cv2.imshow("Imagem Original", img)

#Suavização por cálculo da média
img = img[::2,::2] # Diminui a imagem

suave = np.vstack([
    np.hstack([img,                  cv2.blur(img, ( 3, 3))]),
    np.hstack([cv2.blur(img, (5,5)), cv2.blur(img, ( 7, 7))]),
    np.hstack([cv2.blur(img, (9,9)), cv2.blur(img, (11, 11))]),
    ])

cv2.imshow("Imagem original e Imagens suavisadas (Blur)", suave)
cv2.waitKey(0)

#Suavização pela Gaussiana

suave = np.vstack([
    np.hstack([img, cv2.GaussianBlur(img, ( 3, 3), 0)]),
    np.hstack([cv2.GaussianBlur(img, ( 5, 5), 0), cv2.GaussianBlur(img, ( 7, 7), 0)]),
    np.hstack([cv2.GaussianBlur(img, ( 9, 9), 0), cv2.GaussianBlur(img, (11, 11), 0)]),
    ])

cv2.imshow("Imagem original e suavisadas pelo filtro Gaussiano", suave)
cv2.waitKey(0)

#Suavização pela mediana

suave = np.vstack([
    np.hstack([img, cv2.medianBlur(img, 3)]),
    np.hstack([cv2.medianBlur(img, 5), cv2.medianBlur(img, 7)]),
    np.hstack([cv2.medianBlur(img, 9), cv2.medianBlur(img, 11)]),
    ])

cv2.imshow("Imagem original e suavisadas pela mediana", suave)
cv2.waitKey(0)

#Suavização com filtro bilateral

suave = np.vstack([ np.hstack([img, cv2.bilateralFilter(img, 3, 21, 21)]),
                    np.hstack([cv2.bilateralFilter(img, 5, 35, 35), cv2.bilateralFilter(img, 7, 49, 49)]),
                    np.hstack([cv2.bilateralFilter(img, 9, 63, 63), cv2.bilateralFilter(img, 11, 77, 77)])
                    ])

cv2.imshow("Imagem original e suavisadas pela bilateral", suave)
cv2.waitKey(0)



