import cv2
import numpy as np

def getContoursFilter(img, blur=(7,7), theresfold=100, sizes=""):

    imgFiltered = img.copy()
    if sizes:
        imgFiltered = cv2.resize(imgFiltered, sizes)
    imgFiltered = cv2.cvtColor(imgFiltered, cv2.COLOR_BGR2GRAY)
    imgFiltered = cv2.GaussianBlur(imgFiltered, blur, 1) # Borrando imagem (pra deixar mais fácil)
    imgFiltered = cv2.Canny(imgFiltered, theresfold, theresfold)
    imgFiltered = cv2.dilate(imgFiltered, np.ones((3,3), np.uint8), iterations=1)

    return imgFiltered