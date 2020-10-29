import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

mycolor = []

def findColor(img):
    img = cv2.resize(img, (400, 300))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # Mask give us filtered out imae of that color
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("image", mask)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break