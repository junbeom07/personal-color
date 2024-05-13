import cv2 
import numpy as np

# 얼굴과 눈을 인식하기 위한 xml 파일을 읽음
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 이미지를 읽고 gray scale 로 변경
image = cv2.imread('image.jpg')


# 이미지 사이즈 변경 
new_width = 590
new_height = 737
image = cv2.resize(image, (new_width, new_height))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# 이미지에서 얼굴 인식
faces = face_cascade.detectMultiScale(gray, 1.3, 1)


# 감지된 얼굴에 사각형 그리고 중앙값과 평균값 계산
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # 사각형 부분의 이미지 추출
    roi = image[y:y+h, x:x+w]
    # HSV로 변환
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # 중앙값 계산
    h_median = np.median(hsv_roi[:, :, 0])
    s_median = np.median(hsv_roi[:, :, 1])
    v_median = np.median(hsv_roi[:, :, 2])
    # 평균값 계산 및 소수점 둘째 자리에서 반올림
    h_mean = round(np.mean(hsv_roi[:, :, 0]), 2)
    s_mean = round(np.mean(hsv_roi[:, :, 1]), 2)
    v_mean = round(np.mean(hsv_roi[:, :, 2]), 2)
    print("사각형 부분의 중앙값(HSV):")
    print("Hue:", h_median, "Saturation:", s_median, "Value:", v_median)
    print("사각형 부분의 평균값(HSV):")
    print("Hue:", h_mean, "Saturation:", s_mean, "Value:", v_mean)



# 결과를 화면에 표시함
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()