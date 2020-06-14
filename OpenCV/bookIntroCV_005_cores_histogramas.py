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
cv2.imshow("Imagem Original", img)

#Espaços de Cores
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Cinza", gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b", lab)
cv2.waitKey(0)

#Canais da imagem colorida
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)
resultado = cv2.merge([canalAzul, canalVerde, canalVermelho])
cv2.imshow("Merge", resultado)

zeros = np.zeros(img.shape[:2], dtype = "uint8")
cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
cv2.waitKey(0)

#Histogramas e equalização de imagem
#Função calcHist para calcular o hisograma da imagem
h = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.show()
plt.hist(gray.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)

#Separa os canais
canais = cv2.split(img)
cores = ("b", "g", "r")
plt.figure()
plt.title("'Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
for (canal, cor) in zip(canais, cores):
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, cor)
    plt.xlim([0, 256])
plt.show()

#Equalização de Histograma
h_eq = cv2.equalizeHist(gray)
plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()
plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(gray.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()
cv2.imshow("Cinza", gray)
cv2.imshow("Equalizado", h_eq)
cv2.waitKey(0)



