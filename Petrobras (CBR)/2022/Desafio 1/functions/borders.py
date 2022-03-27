import cv2
import numpy as np

def arenaContourDetection(img, originalImg):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

    planImage = originalImg.copy() # Save the results

    areas = []
    for count in contours:
        area = cv2.contourArea(count)
        areas.append(area)
        
    if max(areas) < 320000: # Only bigger than (800x800/2), returning error if not
        print('Error')
        return -1
    
    #print(max(areas))

    arenaBorder = contours[areas.index(max(areas))] # Getting the bigger area
    
    perimeter = cv2.arcLength(arenaBorder, True) # (border, True)
    #print(perimeter)
    approx = cv2.approxPolyDP(arenaBorder, 0.02*perimeter, True) # (border, I don't know, True)
    vertices = len(approx)
    #print(vertices)
    x, y, w, h = cv2.boundingRect(approx) # Get the position of the Object, with x, y, width and height

    # Planificando imagem e cortando apenas para o terreno
    width, height = 800, 800 # tamanhos da arena
    point1 = np.float32([[x,y],[x+w,y],[x,y+h],[x+w,y+h]]) # Position of the outdoor (the 4 points of it)
    point2 = np.float32([[0,0],[width, 0],[0, height],[width, height]]) # New sizes
    matrix = cv2.getPerspectiveTransform(point1, point2) # Make it plan

    planImage = cv2.warpPerspective(originalImg, matrix, (width, height)) # Turn it into an image

    cv2.rectangle(planImage, (0, 0), (800, 800), (0, 0, 0), 5) # Borders draw
    
    return planImage


def ContourDetection(img, originalImg):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    # (image, mode, method), mode have a lot of options, method it's the way you want the return data to be.

    imgContour = originalImg.copy() # Save the results
    positions = [] # Each will be ('type', x, y) positions of the center

    areas = []
    for count in contours:
        area = cv2.contourArea(count)
        if area > 50:
            areas.append(area)
    
    if len(areas) != 6: # Erro
        print('Error')
        return -1

    for count in contours:
        area = cv2.contourArea(count)
        #print(area)
        if area > 50: # Avoid errors
            #cv2.drawContours(imgContour, count, -1, (0, 255, 0), 3) 
            # (img to put contour, border, -1 is to display all of the contour, color of the border, thickness)
            perimeter = cv2.arcLength(count, True) # (border, True)
            #print(perimeter)
            approx = cv2.approxPolyDP(count, 0.02*perimeter, True) # (border, I don't know, True)
            vertices = len(approx)
            #print(vertices)
            x, y, w, h = cv2.boundingRect(approx) # Get the position of the Object, with x, y, width and height
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 255, 0), 2)
            # We can save that information to calculate the object's position

            # Putting the name of the object in it
            if area == max(areas) : objectType = "Base costeira" 
            else: objectType = "Base terrestre"
            #else: objectType = "?"

            #realPositionX = ((x+w)/2)

            positions.append((objectType, x+w/2, y+h/2))
            cv2.circle(imgContour, (int(x+w/2), int(y+h/2)), 5, (0, 0, 255), 5)

            cv2.putText(imgContour, objectType, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0,0,0))
    
    return imgContour, positions