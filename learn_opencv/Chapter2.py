import cv2
import numpy as np

img = cv2.imread('lena.png')
kernel = np.ones((5, 5), np.uint8)

# Gray Scale, Blur
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, ksize=(7, 7), sigmaX=0)
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgErode)
cv2.waitKey(3000)


