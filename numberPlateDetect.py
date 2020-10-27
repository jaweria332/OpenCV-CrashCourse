import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
platecascade = cv2.CascadeClassifier("E:\\CVDL\\OPENCV_CRASH\\OpenCV-CrashCourse\\haarcascade_russian_plate_number.xml")
minArea = 500
color =0,0,255

while True:
    success, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlate=platecascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in numberPlate:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
            cv2.putText(img, "Number Plate", (x, y-5), (cv2.FONT_HERSHEY_COMPLEX_SMALL), 1,color,2)

            imgROI = img[y:y+h, x:x+w]
            cv2.imshow("ROI", imgROI)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break