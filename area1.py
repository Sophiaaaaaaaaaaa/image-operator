import cv2
import numpy as np
def areaCal(contour):

    area = 0
    for i in range(len(contour)):
        area += cv2.contourArea(contour[i])

    return area
img=cv2.imread(r'C://Users//lizhuocheng//Desktop//cell.jpg')
canny=cv2.Canny(img,100,1000,apertureSize=5,L2gradient=True)
blurred = cv2.blur(canny, (9, 9))
(_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('canny',thresh)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closed',closed)
contours, hierarchy = cv2.findContours(closed,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
cv2.drawContours(img,contours,-1,(0,0,255),3)
#绘制结果
cv2.imshow("result", img)
cnt = contours[0]
area=cv2.contourArea(cnt)
print(area)
cv2.waitKey(0)