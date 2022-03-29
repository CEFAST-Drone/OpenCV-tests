import cv2
import numpy as np
from functions import stack

# Contour detection Function
def ContourDetection(img, originalImg):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    # (image, mode, method), mode have a lot of options, method it's the way you want the return data to be.

    imgContour = originalImg.copy() # Save the results

    for count in contours:
        area = cv2.contourArea(count)
        print(area)
        if area > 50: # Avoid errors
            cv2.drawContours(imgContour, count, -1, (0, 255, 0), 3) 
            # (img to put contour, border, -1 is to display all of the contour, color of the border, thickness)
            perimeter = cv2.arcLength(count, True) # (border, True)
            print(perimeter)
            approx = cv2.approxPolyDP(count, 0.02*perimeter, True) # (border, I don't know, True) Borders of the shape
            """ Each border can be used in this way [x, y], but you must remember that the borders can be in a different order than you expect
            border1 = [approx[0][0][0], approx[0][0][1]]
            border2 = [approx[1][0][0], approx[1][0][1]]
            border3 = [approx[2][0][0], approx[2][0][1]]
            border4 = [approx[3][0][0], approx[3][0][1]]
            Border 1 can be the upper left, 2 can be lower left or .... So don't believe too much on these
            """
            vertices = len(approx)
            print(vertices)
            x, y, w, h = cv2.boundingRect(approx) # Get the position of the Object, with x, y, width and height
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 255, 0), 2)
            # We can save that information to calculate the object's position

            # Putting the name of the object in it
            if vertices == 3: objectType = "Triangle"
            elif vertices == 4: objectType = "Rectangle"
            elif vertices == 8: objectType = "Circle"
            else: objectType = "?"
            cv2.putText(imgContour, objectType, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.2, (0,0,0))
    
    return imgContour

img = cv2.imread("test-resources/shapes.png")

# Contours detection ("bordas") 

# First, filtering the image to get easier to detect Borders
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Black and white image
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1) # Blur image -> Easier and faster to use
imgCanny = cv2.Canny(img, 100, 100) # Contour detection

imgResult = ContourDetection(imgCanny, img)

#cv2.imshow("Original Image", img)
#cv2.imshow("Sent Image", imgCanny)
#cv2.imshow("Final Image", imgResult)

imgStack = stack.concat_tile_resize([[img, imgResult]])
cv2.imshow("Stack Images", imgStack)

cv2.waitKey(0)