#-----------------------------------IMAGE READING---------------------------------------#
#Importing libraries
import cv2

#Reading images
img = cv2.imread('lena.jpg')

#Displaying image
cv2.imshow("Lena", img)

#Wait indefinitely
cv2.waitKey(0)

#-----------------------------------VIDEO READING---------------------------------------#

#Reading video
cap = cv2.videoCapture()

#Displaying video
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
