import cv2
import numpy as np

def calculate_saturation(image_path):
    # 이미지를 읽어옵니다
    image = cv2.imread(image_path)
    
    # 이미지를 HSV 색 공간으로 변환합니다
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # HSV 이미지에서 'S' 채널을 추출합니다
    saturation_channel = hsv_image[:, :, 1]
    
    # 'S' 채널의 평균 값을 계산합니다
    average_saturation = np.mean(saturation_channel)
    
    return average_saturation

# 이미지 파일 경로를 입력하세요
image_path = 'vy.PNG'
saturation = calculate_saturation(image_path)
print(f"Average Saturation: {saturation}")
