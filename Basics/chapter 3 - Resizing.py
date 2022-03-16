import cv2

img = cv2.imread("test-resources\street.jpg")
# print(img.shape) - give us the sizes of the image (height, width, levels of colors)

imgResized = cv2.resize(img, (200, 500)) # (width, height)

cv2.imshow("Resized image", imgResized)

cv2.waitKey(0)