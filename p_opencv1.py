import cv2

img_path = "D:/coding/practice/download.jpg" 
#사진의 파일 위치 (영어만 가능함)
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
cv2.imshow("bangdream", cv2.cvtColor(img, cv2.IMREAD_COLOR))
#사진을 앞의 주황색 이름의 창으로 띄우기
cv2.waitKey()
cv2.destroyAllWindows()