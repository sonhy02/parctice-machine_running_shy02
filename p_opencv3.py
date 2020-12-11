import cv2

def nothing(x):
    pass


cv2.namedWindow('binary')
cv2.createTrackbar('threshold', 'binary',0,225, nothing)
cv2.setTrackbarPos('threshold','binary' ,120 )
img_path = "D:/coding/practice/download.jpg" 
#사진의 파일 위치 (영어만 가능함)
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
cv2.imshow('color',img)

cv2.waitKey()


cv2.imshow('gray',cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
cv2.waitKey()

while(True):
     low=cv2.getTrackbarPos('threshold','binary')
     ret,img_result2 = cv2.threshold(img, low, 255, cv2.THRESH_BINARY)
    #사진을 이진화 시키는 코드
     cv2.imshow('binary',img_result2)
     if cv2.waitKey(1)&0xFF ==27:
         break



cv2.destroyAllWindows()