import cv2

def get_brightness(image):
    # 이미지를 HSV 형식으로 변환
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 명도 값을 가져옴
    value = hsv_image[:,:,2].mean()
    
    return value

# 이미지를 로드
image = cv2.imread('bg.png')

# 명도 값을 가져옴
brightness = get_brightness(image)

print("이미지의 명도:", brightness)
