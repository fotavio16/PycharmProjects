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

#Binarização com limiar
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)

'''
resultado = np.vstack([
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
    ])
'''
resultado = np.vstack([
    np.hstack([img, suave]),
    np.hstack([bin, binI])
    ])

cv2.imshow("Binarização da imagem", resultado)
cv2.waitKey(0)

#Threshold adaptativo

bin1 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)
bin2 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)

resultado = np.vstack([
    np.hstack([img, suave]),
    np.hstack([bin1, bin2])
    ])
cv2.imshow("Binarização adaptativa da imagem", resultado)
cv2.waitKey(0)

#Threshold com Otsu e Riddler-Calvard
'''
T = mahotas.thresholding.otsu(suave)
temp = img.copy()
temp[temp > T] = 255
temp[temp < 255] = 0
temp = cv2.bitwise_not(temp)
T = mahotas.thresholding.rc(suave)
temp2 = img.copy()
temp2[temp2 > T] = 255
temp2[temp2 < 255] = 0
temp2 = cv2.bitwise_not(temp2)
resultado = np.vstack([
    np.hstack([img, suave]),
    np.hstack([temp, temp2])
    ])
cv2.imshow("Binarização com método Otsu e Riddler-Calvard", resultado)
cv2.waitKey(0)
'''

