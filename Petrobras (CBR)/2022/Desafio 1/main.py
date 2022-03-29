import cv2
import numpy as np
from functions import stack
from functions import filters
from functions import borders

path = 'test-resources/arenaTorta2.png'
img = cv2.imread(path) # Getting Image

#img = cv2.resize(img, (800, 800))

# Filters to improve
imgFiltered = filters.getContoursFilter(img)

# "Planificando"/Wrapping image

planImage = borders.arenaContourDetection(imgFiltered, img)
planImageFiltered = filters.getContoursFilter(planImage)

# Detectin of "base costeira e bases terrestres"

detectedImage, positions = borders.ContourDetection(planImageFiltered, planImage) 
detectedImage = cv2.resize(detectedImage, (400, 400)) # Better view

for pos in positions: # Position of the center (type, x, y) # x and y are in centimeters(cm)
    print(pos)

# Results show

resultImg = stack.join([
        [img, detectedImage]
    ])

cv2.imshow("Analise", resultImg)
#planImageFiltered = cv2.resize(planImageFiltered, (400, 400))
cv2.imshow("Filtered Image", planImage)


cv2.waitKey(0)