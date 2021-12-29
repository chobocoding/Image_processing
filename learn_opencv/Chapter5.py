import cv2
import numpy as np

img = cv2.imread('cards.jpg')
# 출력할 이미지의 너비, 높이
width, height = 250, 350

# 4개의 점을 기반으로 WarpPerspective 
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)