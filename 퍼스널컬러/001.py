import cv2
import numpy as np

# 얼굴 데이터 xml 파일
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 이미지를 읽음
image = cv2.imread('tjwkdgns.jpg')

# 표준 크기에 맞춰 비율을 유지하면서 크기 조정
standard_width = 800
standard_height = 600

original_height, original_width = image.shape[:2]
aspect_ratio = original_width / original_height

if aspect_ratio > 1:
    new_width = standard_width
    new_height = int(standard_width / aspect_ratio)
else:
    new_height = standard_height
    new_width = int(standard_height * aspect_ratio)
resized_image = cv2.resize(image, (new_width, new_height))

# 얼굴인식
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 1)

# 감지된 얼굴에 사각형 그리고 평균값 계산
for (x, y, w, h) in faces:
    cv2.rectangle(resized_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # 사각형 부분의 이미지 추출
    roi = resized_image[y:y+h, x:x+w]
    # HSV로 변환
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # 평균값 계산 및 소수점 둘째 자리에서 반올림
    h_mean = round(np.mean(hsv_roi[:, :, 0]), 2)
    s_mean = round(np.mean(hsv_roi[:, :, 1]), 2)
    v_mean = round(np.mean(hsv_roi[:, :, 2]), 2)
    print("사각형 부분의 평균값(HSV):")
    print("Hue:", h_mean, "Saturation:", s_mean, "Value:", v_mean)

    # 중앙에 위치한 작은 사각형의 크기 계산
    small_w = w // 2
    small_h = h // 2
    small_x = x + w // 4
    small_y = y + h // 4
    
    # 작은 사각형 (정확도)
    cv2.rectangle(resized_image, (small_x, small_y), (small_x+small_w, small_y+small_h), (0, 255, 0), 2)
    small_roi = resized_image[small_y:small_y+small_h, small_x:small_x+small_w]
    hsv_small_roi = cv2.cvtColor(small_roi, cv2.COLOR_BGR2HSV)
    small_h_mean = round(np.mean(hsv_small_roi[:, :, 0]), 2)
    small_s_mean = round(np.mean(hsv_small_roi[:, :, 1]), 2)
    small_v_mean = round(np.mean(hsv_small_roi[:, :, 2]), 2)
    print("중앙 작은 사각형 부분의 평균값(HSV):")
    print("Hue:", small_h_mean, "Saturation:", small_s_mean, "Value:", small_v_mean)

def evaluate_values(small_v_mean, small_s_mean):
    results = []

    # 퍼스널컬러 범위 (수정 필요)
    if 255 >= small_v_mean >= 181:
        if 0 <= small_s_mean <= 90:
            results.append('p')
        if 90 <= small_s_mean <= 170:
            results.append('lt')
    if 218 >= small_v_mean >= 141:
        if 188 <= small_s_mean <= 243:
            results.append('b')
    if 181 >= small_v_mean >= 101:
        if 0 <= small_s_mean <= 122:
            results.append('ltg')
        if 122 <= small_s_mean <= 198:
            results.append('sf')
    if 141 >= small_v_mean >= 66:
        if 210 <= small_s_mean <= 243:
            results.append('sv')
    if 101 >= small_v_mean >= 31:
        if 0 <= small_s_mean <= 160:
            results.append('g')
        if 160 <= small_s_mean <= 206:
            results.append('d')
    if 66 >= small_v_mean >= 16:
        if 215 <= small_s_mean <= 231:
            results.append('dp')
    if 31 >= small_v_mean >= 0:
        if 176 <= small_s_mean <= 217:
            results.append('dkg')
        if 217 <= small_s_mean <= 238:
            results.append('dk')

    # 결과 출력
    if results:
        print(', '.join(results))
    else:
        print('재시도')

evaluate_values(small_v_mean, small_s_mean)

# 결과를 화면에 표시함
cv2.imshow('image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
