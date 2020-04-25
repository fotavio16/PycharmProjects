'''

  Livro-Introdução-a-Visão-Computacional-com-Python-e-OpenCV-3

Repositório de imagens
https://github.com/opencv/opencv/tree/master/samples/data
'''

import cv2
import numpy as np

VERMELHO = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL = (255, 0, 0)
AMARELO = (0, 255, 255)
BRANCO = (255,255,255)
CIANO = (255, 255, 0)
PRETO = (0, 0, 0)

img = cv2.imread('ponte2.jpg') # Flag 1 = Color, 0 = Gray, -1 = Unchanged
cv2.imshow("Imagem Original", img)
cv2.waitKey(0)

#Cria um retangulo azul por toda a largura da imagem
img[30:50, :] = AZUL

#Cria um quadrado vermelho
img[100:150, 50:100] = VERMELHO

#Cria um retangulo amarelo por toda a altura da imagem
img[:, 200:220] = AMARELO

#Cria um retangulo verde da linha 150 a 300 nas colunas 250 a 350
img[150:300, 250:350] = VERDE

#Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a 350
img[300:400, 50:150] = CIANO

#Cria um quadrado branco
img[250:350, 300:400] = BRANCO

#Cria um quadrado preto
img[70:100, 300: 450] = (0, 0, 0)

cv2.imshow("Imagem com Desenhos", img)
#cv2.imwrite("alterada.jpg", img)
cv2.waitKey(0)

img = cv2.imread('ponte2.jpg')

cv2.line(img, (0, 0), (100, 200), VERDE)
cv2.line(img, (300, 200), (150, 150), VERMELHO, 5)
cv2.rectangle(img, (20, 20), (120, 120), AZUL, 10)
cv2.rectangle(img, (200, 50), (225, 125), VERDE, -1)

(X, Y) = (img.shape[1] // 2, img.shape[0] // 2)
for raio in range(0, 175, 15):
  cv2.circle(img, (X, Y), raio, VERMELHO)

cv2.imshow("Desenhando na Imagem", img)
cv2.waitKey(0)

img = cv2.imread('ponte2.jpg')

fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(15,65), fonte, 2, VERMELHO, 2 , cv2.LINE_AA)

cv2.imshow("Escrevendo na Imagem", img)
cv2.waitKey(0)