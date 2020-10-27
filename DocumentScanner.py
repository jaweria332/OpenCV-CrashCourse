import cv2
import numpy as np

widthImg = 640
heightImg = 480
cap = cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4, heightImg)
cap.set(10, 150)

def preprocessingData(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),1)
    edges = cv2.Canny(blur, 200, 200)
    #Adding dialtion to thinner the edges
    kernel=np.ones((5,5))
    dialation = cv2.dilate(edges, kernel, iterations=1)

    #Eroding the image
    imgThresh = cv2.erode(dialation, kernel, iterations=1)

    return imgThresh

while True:
    success, img = cap.read()
    cv2.resize(img, (widthImg, heightImg))
    imgthresh = preprocessingData(img)
    cv2.imshow("Result", imgthresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break