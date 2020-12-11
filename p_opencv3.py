import cv2

def nothing(x):
    pass


cv2.namedWindow('binary')
cv2.createTrackbar('threshold','binary',0,225, nothing)
cv2.setTrackbarPos('threshold','binary' ,120 )
#트랙바 만드는 코드

img_path = "D:/coding/practice/download.jpg" 
#사진의 파일 위치 (영어만 가능함)
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('color',img)

cv2.waitKey()

cv2.imshow('gray',cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
cv2.waitKey()

while(True):
     low=cv2.getTrackbarPos('threshold','binary')
     ret,img_result2 = cv2.threshold(gray, low, 255, cv2.THRESH_BINARY)
    #사진을 이진화 시키는 코드
     cv2.imshow('binary',img_result2)
     if cv2.waitKey()&0xFF ==27:
         break
#트랙바 적용시킨 경우

cv2.destroyAllWindows()