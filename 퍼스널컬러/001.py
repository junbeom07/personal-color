import cv2
import numpy as np

image = cv2.imread('image.jpg')

# 새로운 이미지 크기 정의 (새로운 너비, 새로운 높이)
new_width = 590
new_height = 737
resized_image = cv2.resize(image, (new_width, new_height))



hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

x, y = 100, 100

h, s, v = hsv_image[y, x]

print("Hue:", h)
print("Saturation:", s)
print("Value:", v)

cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()