import cv2 

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

# 검출된 얼굴 개수만큼 for 루프 동작
for (x,y,w,h) in faces:

    # 원본 이미지의 얼굴 위치에 사각형 그리기
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)







# 결과를 화면에 표시함
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()