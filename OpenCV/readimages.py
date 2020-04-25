'''

Repositório de imagens
https://github.com/opencv/opencv/tree/master/samples/data
'''

import cv2

img = cv2.imread('lena.jpg', -1) # Flag 1 = Color, 0 = Gray, -1 = Unchanged
cv2.imshow('image', img) # 'image' = nome da janela
# cv2.waitKey(5000) # mostra imagem por 5 segundos
k = cv2.waitKey(0)

if k == 27: # escape key
  cv2.destroyAllWindows()
elif k == ord('s'): # s key
  cv2.imwrite('lena_copy.png', img)
  cv2.destroyAllWindows()

