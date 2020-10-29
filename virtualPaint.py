import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

mycolor = [[0, 128, 188,255,0,255]]

def findColor(img):
    img = cv2.resize(img, (400, 300))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(mycolor[0][0:3])
    upper = np.array(mycolor[0][3:6])
    # Mask give us filtered out image of that color
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow(str(mycolor), mask)

def getContour(img):
    contour, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area> 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, mycolor)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break