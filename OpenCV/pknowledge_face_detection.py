import cv2

#Define o classificador
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
#cap = cv2.VideoCapture('test.mp4')
img1 = cv2.imread('faces2.jpg')
img2 = cv2.imread('faces3.jpg')
img3 = cv2.imread('facesMatrix.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

#Detecção
faces1 = face_cascade.detectMultiScale(gray1, 1.1, 4)
faces2 = face_cascade.detectMultiScale(gray2, 1.1, 4)
faces3 = face_cascade.detectMultiScale(gray3, 1.1, 4)

#Desenha os retângulos
for (x, y, w, h) in faces1:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 3)
for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 3)
for (x, y, w, h) in faces3:
    cv2.rectangle(img3, (x, y), (x + w, y + h), (255, 0, 0), 3)

# Redimensiona as imagens 1 e 2
img1 = img1[::3, ::3]
img2 = img2[::3, ::3]

# Display the output
cv2.imshow('Imagem 1', img1)
cv2.imshow('Imagem 2', img2)
cv2.imshow('Imagem 3', img3)

cv2.waitKey(0)

'''
while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
'''

