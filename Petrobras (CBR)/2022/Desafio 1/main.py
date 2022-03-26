import cv2
import numpy as np
from functions import stack
from functions import filters
from functions import borders

path = 'test-resources/arena.png'
img = cv2.imread(path) # Getting Image

img = cv2.resize(img, (800, 800))

# Filters to improve
imgFiltered = filters.getContoursFilter(img)

# Planificando imagem

planImage = borders.arenaContourDetection(imgFiltered, img)
planImage = cv2.resize(planImage, (400, 400)) # Melhor visualização
planImageFiltered = filters.getContoursFilter(planImage)

# Detecção da base costeira e terrestres

detectedImage = borders.ContourDetection(planImageFiltered, planImage) 
# ?????? Falta conseguir pegar as posições das formas encontradas

# Printando na tela resultados

resultImg = stack.join([
        [img, detectedImage]
    ])

cv2.imshow("Analise", resultImg)


cv2.waitKey(0)