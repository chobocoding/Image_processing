import cv2

# Read image
# img = cv2.imread('lena.png')
# cv2.imshow("Output", img)
# cv2.waitKey(5000) #msec

# Read Video
# cap = cv2.VideoCapture('video.mp4')
# 
# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Read Webcap
cap = cv2.VideoCapture(0) # 0 >> 노트북 내장 웹캠
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100) # 밝기 설정
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
