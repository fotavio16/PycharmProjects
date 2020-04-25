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

#Cortando uma imagem / Crop
recorte = img[100:200, 100:200]
cv2.imshow("Recorte da imagem", recorte)
cv2.waitKey(0)

#Redimensionamento / Resize
img = cv2.imread('ponte2.jpg')
largura = img.shape[1]
altura = img.shape[0]
proporcao = float(altura/largura)
largura_nova = 320 #em pixels
altura_nova = int(largura_nova * proporcao)
tamanho_novo = (largura_nova, altura_nova)
img_redimensionada = cv2.resize(img, tamanho_novo, interpolation = cv2.INTER_AREA)
cv2.imshow('Resultado', img_redimensionada)
cv2.waitKey(0)

#Slicing
img = cv2.imread('ponte2.jpg')
img_redimensionada = img[::2,::2]
cv2.imshow("Imagem redimensionada", img_redimensionada)
cv2.waitKey(0)

#Espelhando uma imagem / Flip
img = cv2.imread('ponte2.jpg')
flip_horizontal = img[::-1,:] #comando equivalente abaixo
# #flip_horizontal = cv2.flip(img, 1)

cv2.imshow("Flip Horizontal", flip_horizontal)
flip_vertical = img[:,::-1] #comando equivalente abaixo
# #flip_vertical = cv2.flip(img, 0)

cv2.imshow("Flip Vertical", flip_vertical)
flip_hv = img[::-1,::-1] #comando equivalente abaixo
# #flip_hv = cv2.flip(img, -1)
cv2.imshow("Flip Horizontal e Vertical", flip_hv)
cv2.waitKey(0)

#Rotacionando uma imagem / Rotate
img = cv2.imread('ponte2.jpg')
(alt, lar) = img.shape[:2] #captura altura e largura
centro = (lar // 2, alt // 2) #acha o centro

M = cv2.getRotationMatrix2D(centro, 30, 1.0) #30 graus
img_rotacionada = cv2.warpAffine(img, M, (lar, alt))

cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)
cv2.waitKey(0)

#Máscaras
img = cv2.imread('ponte2.jpg')
mascara = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 100, 255, -1)
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)

cv2.imshow("Máscara aplicada à imagem", img_com_mascara)
cv2.waitKey(0)

img = cv2.imread('ponte2.jpg')
mascara = np.zeros(img.shape[:2], dtype = "uint8")
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 180, 255, 70)
cv2.circle(mascara, (cX, cY), 70, 255, -1)
cv2.imshow("Máscara", mascara)
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)

cv2.imshow("Máscara aplicada à imagem", img_com_mascara)
cv2.waitKey(0)




