import cv2

img_path = "D:/coding/practice/download.jpg" 
#사진의 파일 위치 (영어만 가능함)
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
cv2.imshow('bangdream',img)

cv2.waitKey()



cv2.imshow('bangdream',cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
cv2.waitKey()

ret,img_result2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('bangdream',img_result2)
cv2.waitKey()

cv2.destroyAllWindows()