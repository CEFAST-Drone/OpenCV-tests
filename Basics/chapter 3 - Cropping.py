import cv2

img = cv2.imread("test-resources\street.jpg")
 
# Cropping is cutting the image (getting just a part of it)

imgCropped = img[0:100, 100:250] # height, width

cv2.imshow("Cropped image", imgCropped)

cv2.waitKey(0)