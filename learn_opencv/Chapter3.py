import cv2
import numpy as np

img = cv2.imread('lambo.png')
print(img.shape) # 462, 623, 3 

imgResize = cv2.resize(img, (300, 200)) # (width, height)
print(imgResize.shape) # 200, 300, 3 > (height, width ,channel)

imgCropped = img[:200, 200:500]
print(imgCropped.shape)

cv2.imshow('image origin', img)
cv2.imshow('image Resize', imgResize)
cv2.imshow('image Cropped', imgCropped)

cv2.waitKey(0)