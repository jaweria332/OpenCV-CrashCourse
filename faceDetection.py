import cv2
import numpy as np

facecascade = cv2.CascadeClassifier("E:\\TRY_ON_VIRTUAL\\Step_1_face_recognize\\haarcascade_frontalface_default.xml")
img = cv2.imread("lena.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = facecascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)