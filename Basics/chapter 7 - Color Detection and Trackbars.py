import cv2
import numpy as np

"""
 Manual filter parameters defination
 Images on Notion
 Hue -> pure spectrum colors ("cores do arco-iris") being red, orange, yellow, blue, green and violet, it goes from 0 to 360 (or 0 to 179)
 Saturation -> Intensity of the color (0 to 100%, or 0 to 255)
 Value -> Brightness (0 to 100% or 0 to 255)
"""

lowerFilters = np.array([0, 0, 0]) # hue min, saturation min, value min
upperFilters = np.array([360, 255, 255])

def onChange(value): # On change function (not used here, but can be used)
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 600, 300)
cv2.createTrackbar("Hue min", "Trackbars", 0, 360, onChange)
cv2.createTrackbar("Hue max", "Trackbars", 360, 360, onChange)
cv2.createTrackbar("Sat min", "Trackbars", 0, 255, onChange)
cv2.createTrackbar("Sat max", "Trackbars", 255, 255, onChange)
cv2.createTrackbar("Val min", "Trackbars", 0, 255, onChange)
cv2.createTrackbar("Val max", "Trackbars", 255, 255, onChange)

while True:
    img = cv2.imread("test-resources/eraser.png")

    img = cv2.resize(img, (300, 300)) # (width, height)

    # Getting only the (defined range) Color
    # We're going to use Trackbars (scroll bars), to set the minimum and maximum values of the blue color (optimizing it with trackbars)

    lowerFilters[0] = cv2.getTrackbarPos("Hue min", "Trackbars") # scroll name, window of trackbar name
    lowerFilters[1] = cv2.getTrackbarPos("Sat min", "Trackbars")
    lowerFilters[2] = cv2.getTrackbarPos("Val min", "Trackbars")
    upperFilters[0] = cv2.getTrackbarPos("Hue max", "Trackbars")
    upperFilters[1] = cv2.getTrackbarPos("Sat max", "Trackbars")
    upperFilters[2] = cv2.getTrackbarPos("Val max", "Trackbars")

    mask = cv2.inRange(img, lowerFilters, upperFilters) # Filter being applied (0 = Black, 1 = White, 1 to match the range defined)
    imgResults = cv2.bitwise_and(img, img, mask=mask) # Put the colors in the 1 (positive binaries) places

    cv2.imshow("Eraser Image", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filter Image", imgResults)

    cv2.waitKey(1) # Delay