import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('image.jpg')

# BGR을 HSV로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV 값 변경 (예: Hue 값을 30만큼 증가)
hsv_image[:, :, 0] = (hsv_image[:, :, 0] + 30) % 180  # Hue 값은 0에서 179 사이로 제한됨

# HSV를 BGR로 다시 변환
modified_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# 결과 이미지 출력
cv2.imshow('Modified Image', modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
