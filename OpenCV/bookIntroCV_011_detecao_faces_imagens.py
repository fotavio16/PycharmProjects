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

#Carrega arquivos e converte para tons de cinza
img1 = cv2.imread('faces2.jpg')
img2 = cv2.imread('faces3.jpg')
img3 = cv2.imread('facesMatrix.jpg')
imgPB1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imgPB2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
imgPB3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

#Criação do detector de faces
df = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Executa a detecção
faces1 = df.detectMultiScale(imgPB1, scaleFactor = 1.05, minNeighbors = 7, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)
faces2 = df.detectMultiScale(imgPB2, scaleFactor = 1.05, minNeighbors = 7, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)
faces3 = df.detectMultiScale(imgPB3, scaleFactor = 1.05, minNeighbors = 7, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)

#Desenha retangulos amarelos na iamgem original (colorida)
for (x, y, w, h) in faces1:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 255), 7)
for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 255), 7)
for (x, y, w, h) in faces3:
    cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 255, 255), 2)

#Redimensiona as imagens 1 e 2
img1 = img1[::3,::3]
img2 = img2[::3,::3]

# Exibe imagem. Título da janela exibe número de faces
cv2.imshow(str(len(faces1))+' face(s) encontrada(s).', img1)
cv2.imshow(str(len(faces2))+' face(s) encontrada(s).', img2)
cv2.imshow(str(len(faces3))+' face(s) encontrada(s).', img3)
cv2.waitKey(0)
