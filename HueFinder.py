import cv2
import numpy as np
def empty(a):
    pass

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)


#Defining Trackbar
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbar", 255, 255, empty)


while True:
    _, img = cap.read()
    img = cv2.resize(img, (400, 300))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbar")
    print(h_min, h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min, s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    #Mask give us filtered out imae of that color
    mask = cv2.inRange(imgHSV, lower, upper)

    #Compare bitwise both images and return boolean value ie true or false


    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.waitKey(1)