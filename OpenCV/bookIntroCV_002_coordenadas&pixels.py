'''

  Livro-Introdução-a-Visão-Computacional-com-Python-e-OpenCV-3

Repositório de imagens
https://github.com/opencv/opencv/tree/master/samples/data
'''

import cv2

img = cv2.imread('bridge.jpg') # Flag 1 = Color, 0 = Gray, -1 = Unchanged

(b, g, r) = img[0, 0] # A ordem é BGR

print(f'O pixel (0, 0) tem as seguintes cores: Vermelho: {r},')
print(f'Verde: {g}, e Azul: {b}.')

cv2.imshow('Imagem Original', img)
cv2.waitKey(0)

(lins, cols, lixo) = img.shape
for y in range(0, lins):
  for x in range(0, cols):
    (b, g, r) = img[y, x]
    img[y, x] = ((b+y)%256, (g+y)%256, (r+y)%256)

cv2.imshow("Imagem Modificada", img)
cv2.waitKey(0)

img = cv2.imread('bridge.jpg')
(lins, cols, lixo) = img.shape
for y in range(0, lins, 10):
  for x in range(0, cols, 10):
    img[y:y+5, x:x+5] = (0, 255, 255)

cv2.imshow("Imagem Modificada 2", img)
cv2.waitKey(0)