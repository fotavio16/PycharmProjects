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

#Função para facilitar a escrita nas imagem
def escreve(img, texto, cor=AZUL):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0, cv2.LINE_AA)

img = cv2.imread('dados5.jpg') # Flag 1 = Color, 0 = Gray, -1 = Unchanged

img = img[::2,::2] # Redimensiona a imagem se necessário
imgC2 = img.copy()

#Passo 1 - Converte para tons de cinza
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Passo 2: Blur/Suavização da imagem
suave = cv2.blur(img, (7, 7))

#Passo 3: Binarização resultando em pixels brancos e pretos
#T = mahotas.thresholding.otsu(suave)
#bin = suave.copy()
#bin[bin > T] = 255
#bin[bin < 255] = 0
#bin = cv2.bitwise_not(bin)
#bin = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)
#bin = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)
# Otsu's thresholding
#ret2,bin = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,bin = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Passo 4: Detecção de bordas com Canny
bordas = cv2.Canny(bin, 70, 150)

#Passo 5: Identificação e contagem dos contornos da imagem
# #cv2.RETR_EXTERNAL = conta apenas os contornos externos
(objetos, lx) = cv2.findContours(bordas.copy(),
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#A variável lx (lixo) recebe dados que não são utilizados
print(f'Objetos: {len(objetos)}')

escreve(img, "Imagem em tons de cinza", 0)
escreve(suave, "Suavizacao com Blur", 0)
escreve(bin, "Binarizacao com Metodo Otsu", 255)
escreve(bordas, "Detector de bordas Canny", 255)

temp = np.vstack([
    np.hstack([img, suave ]),
    np.hstack([bin, bordas])
    ])

cv2.imshow("Quantidade de objetos: "+str(len(objetos)), temp)
cv2.waitKey(0)
cv2.imshow("Imagem Original", img)
cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)
escreve(imgC2, str(len(objetos))+" objetos encontrados!")
cv2.imshow("Resultado", imgC2)
cv2.waitKey(0)


