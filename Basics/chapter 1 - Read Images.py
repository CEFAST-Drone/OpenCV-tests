import cv2

#                                   Img Read

img = cv2.imread("./test-resources/street.jpg") # Reading the image (PATH)

print(img) # Real structure of the image

cv2.imshow("Test Window", img) # Displaying the image (Name of the window, image variant)
cv2.waitKey(0) # To not instantly close the Image window, (0 or milisseconds) - 0 is infinit, milisseconds is the time until it go ahead in the coad
