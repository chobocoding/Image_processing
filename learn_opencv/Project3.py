# Number Plate detector - Real Time
import cv2
import numpy as np

nPlatesCascade = cv2.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")
minArea = 1000
maxArea = 5000
color = (255, 0, 255)
# Read Video
cap = cv2.VideoCapture('plates.mp4')

while True:
    success, img = cap.read()
    imgGray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlatesCascade.detectMultiScale(imgGray, 1.1, 4)
    
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea and area < maxArea:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, "Number Plate", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow('ROI', imgRoi)
    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break