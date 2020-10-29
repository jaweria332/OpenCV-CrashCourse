import cv2
import numpy as np
def empty(a):
    pass



#Function to stack images
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


#Defining Trackbar
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 12, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 45, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbar", 253, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 84, 255, empty)
cv2.createTrackbar("Val Max", "Trackbar", 255, 255, empty)

path = "car.jpg"

while True:
    img = cv2.imread(path)
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
    imgRes = cv2.bitwise_and(img, img, mask=mask)

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgRes]))
    cv2.imshow("Stacked Image", imgStack)
    #cv2.imshow("Original", img)
    #cv2.imshow("HSV", imgHSV)
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Result", imgRes)
    cv2.waitKey(1)