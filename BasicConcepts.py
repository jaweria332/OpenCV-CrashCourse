#Importing libraries
import cv2
import numpy as np

#-----------------------------------IMAGE READING---------------------------------------#
#Reading images
img = cv2.imread('lena.jpg')

#Displaying image
#cv2.imshow("Lena", img)

#Wait indefinitely
#cv2.waitKey(0)

#-----------------------------------VIDEO READING---------------------------------------#
"""
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
"""

#-----------------------BASIC FUNCTIONS LIKE GRAY, BLUR, EDGE DETECTOR, DIALATION, ERROTION----------------------------#

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(img, (7,7), 0)
imgEdge = cv2.Canny(img, 100, 100)

kernel=np.ones((3,3) , np.uint8)
imgDial = cv2.dilate(imgEdge, kernel, iterations=1)

imgEroder = cv2.erode(imgDial, kernel, iterations=1)
#Displaying image
cv2.imshow("Lena", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blurImg)
cv2.imshow("Edged", imgEdge)
cv2.imshow("Eroded", imgEroder)

#Wait indefinitely
cv2.waitKey(0)
