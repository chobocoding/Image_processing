import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

# img[:] = 255, 0, 0 # black to blue
# img[200:300, 100:300] = 255, 0, 0

# How to create line
cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 255, 0), 3) # cv.line(img, start point, end point, color, thickness)
cv2.rectangle(img, (0, 0), (256, 256), (0, 0, 255), 5) # thickness=cv2.FILLED로 사각형 내부 채우기 가능
cv2.circle(img, (256, 256), 20, (255, 255, 255), 3) # cv2.circle(image, center poing, radius, color, thickness)
cv2.putText(img, "OpenCV", (00, 240), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)



cv2.imshow('Image', img)
cv2.waitKey(0) 