# Virtual print
import cv2
import numpy as np

# get contours >> 색상의 윤곽선 검출
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y , w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt , 0.02*peri, True)
            x, y , w, h = cv2.boundingRect(approx)
    return x+w//2, y # 윤곽선의 최상단값, 중앙값 반환
            
# Read Webcam
cap = cv2.VideoCapture(0) # 0 >> 노트북 내장 웹캠
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150) # 밝기 설정

# HSV값 경계 설정하여 색상 검출
myColors = [[92, 83, 163, 112, 255, 255], # Blue
            [0, 140, 169, 19, 250, 255],  # Orange
            [71, 67, 65, 95, 163, 211]] # Green

# 각 파랑, 주황, 초록 BGR값
myColorValues = [[255, 0 ,0],
                [51, 153, 255],
                [0, 255, 0]]

# [x. y, colorId]
myPoints = [] 

# 색상 찾기
def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # 색상(H) 채도(S) 명도(V)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        
        # 펜 촉에 원 표시
        cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
        
        # 좌표값 append
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return newPoints

# 그리기
def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
        
    cv2.imshow('Video', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
