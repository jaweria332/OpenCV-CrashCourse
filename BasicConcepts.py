#Importing libraries
import cv2
import numpy as np
"""
#-----------------------------------IMAGE READING---------------------------------------#
#Reading images
img = cv2.imread('lena.jpg')

#Displaying image
#cv2.imshow("Lena", img)

#Wait indefinitely
#cv2.waitKey(0)

#-----------------------------------VIDEO READING---------------------------------------#

#Reading video
cap = cv2.VideoCapture("sample.mp4")

#Displaying video
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#----------------------------------WEBCAME CAPTURING-----------------------------------------#
#Reading video
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
#Displaying video
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#-----------------------BASIC FUNCTIONS LIKE GRAY, BLUR, EDGE DETECTOR, DIALATION, ERROTION----------------------------#

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(img, (7,7), 0)
imgEdge = cv2.Canny(img, 100, 100)

kernel=np.ones((3,3) , np.uint8)
imgDial = cv2.dilate(imgEdge, kernel, iterations=1)

imgEroder = cv2.erode(imgDial, kernel, iterations=1)

imgResize = cv2.resize(img, (300, 300))
imgCropped = img[0:200, 200:500]

#Displaying image
cv2.imshow("Lena", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blurImg)
cv2.imshow("Edged", imgEdge)
cv2.imshow("Eroded", imgEroder)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)


#-------------------------------------------------SHAPES--------------------------------------------------------#
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

#Drawing line
cv2.line(img, (0,0), (250, 250), (0,0,255), 3)
cv2.line(img, (250,250), (512, 0), (0,0,255), 3)
cv2.line(img, (0,0), (512, 0), (0,0,255), 3)

#Drawing Rectangle
cv2.rectangle(img, (200, 200),(300, 300), (255, 0, 255), 5)

#Drawing circle on images
cv2.circle(img, (251, 253), 30, (255, 255, 0), 5)

#Put text
cv2.putText(img, "OPEN HERE", (151,150), cv2.FONT_HERSHEY_COMPLEX,1, (0,150,150), 1)

#######--------------------------------WARP PERSPECTIVE-----------------------############
#defining width and height
width, height=300, 300
pt1 = np.float32([[111, 219], [287, 188], [154, 482], [354, 440]])
pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pt1, pt2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Warp perspective", imgOutput)

###############------------------STACKING THE IMAGES--------------------------------#############
imgH = np.hstack((img, img))
imgV = np.vstack((img, img))
cv2.imshow("Stack", imgH)
cv2.imshow("Stack", imgV)
#Wait indefinitely
cv2.waitKey(0)"""


##############----------------------COLOR DETECTION----------------------------################
def empty(a):
    pass

#Defining Trackbar
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 0, 255, empty)
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
    mask = cv2.inRange(imgHSV, lower, upper)
    imgRes = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.waitKey(1)