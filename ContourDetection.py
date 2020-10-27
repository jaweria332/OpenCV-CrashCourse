import cv2
import numpy as np

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


#Defining a functions to get contour
def getContour(img):
    contours, hier = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgcopy, cnt, -1, (255, 0,0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor == 3:
                objectType = "Triangle"
            elif objCor == 4:
                rat=w/float(h)
                if rat>0.95 and rat < 1.05:
                    objectType="Sqauare"
                else:
                    objectType="Rectangle"
            elif objCor>4:
                objectType="Circle"
            else:
                objectType="None"
            cv2.rectangle(imgcopy, (x,y), (x+w, y+h), (0,0,0), 4)
            cv2.putText(imgcopy, objectType, (x +(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255), 2)

path = 'shapes.jpg'
img = cv2.imread(path)
imgcopy = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Blur = cv2.GaussianBlur(gray, (7,7), 1)
Canny = cv2.Canny(Blur, 50, 50)
getContour(Canny)
blank = np.zeros_like(img)
stack = stackImages(0.4, ([img, gray, Blur], [Canny, imgcopy,blank]))

cv2.imshow("Stack", stack)
cv2.waitKey(0)