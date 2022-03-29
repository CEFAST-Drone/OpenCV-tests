import cv2
import numpy as np

def arenaContourDetection(img, originalImg):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

    planImage = originalImg.copy() # Save the results

    areas = []
    for count in contours:
        area = cv2.contourArea(count)
        areas.append(area)
        
    #if max(areas) < 320000: # Only bigger than (800x800/2), returning error if not
    #    print('Error')
    #    return -1
    
    #print(max(areas))

    arenaBorder = contours[areas.index(max(areas))] # Getting the bigger area
    #cv2.drawContours(originalImg, arenaBorder, -1, (0, 255, 0), 3) 
    
    perimeter = cv2.arcLength(arenaBorder, True) # (border, True)
    #print(perimeter)
    approx = cv2.approxPolyDP(arenaBorder, 0.02*perimeter, True) # (border, I don't know, True)
    vertices = len(approx)
    border1 = [approx[0][0][0], approx[0][0][1]]
    border2 = [approx[1][0][0], approx[1][0][1]]
    border3 = [approx[2][0][0], approx[2][0][1]]
    border4 = [approx[3][0][0], approx[3][0][1]]
    x, y, w, h = cv2.boundingRect(approx) # Get the position of the Object, with x, y, width and height
    # ?????????????????????? Erro

    # Planificando imagem e cortando apenas para o terreno
    width, height = 800, 800 # tamanhos da arena
    point1 = np.float32([border1,border4,border2,border3])
    point2 = np.float32([[0,0],[width, 0],[0, height],[width, height]]) # New sizes
    matrix = cv2.getPerspectiveTransform(point1, point2) # Make it plan

    planImage = cv2.warpPerspective(originalImg, matrix, (width, height)) # Turn it into an image

    cv2.rectangle(planImage, (0, 0), (800, 800), (255, 255, 255), 20) # Borders draw
    
    return planImage


def ContourDetection(img, originalImg):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    # (image, mode, method), mode have a lot of options, method it's the way you want the return data to be.

    imgContour = originalImg.copy() # Save the results
    positions = [] # Each will be ('type', x, y) positions of the center

    areas = []
    info = []
    for count in contours:
        area = cv2.contourArea(count)
        if area > 50:
            areas.append(area)

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

            cv2.circle(imgContour, (int(x+w/2), int(y+h/2)), 5, (0, 0, 255), 5)

            info.append([perimeter, vertices, x, y, w, h])

    
    #if len(areas) != 7: # Erro, não encontrou as 5 bases terrestres, 1 base costeria e o 1 "gasoduto"
    #    print(f'Error\nHá {len(areas)} formas geométricas detectadas')
    #    return -1

    areas.sort(reverse=True) # do maior para o menor

    for index, count in enumerate(contours):
        area = cv2.contourArea(count)
        #print(area)
        if area > 50: # Avoid errors
            # Putting the name of the object in it
            if area == areas[0]: objectType = "Base Costeira" 
            elif area == areas[1]: objectType = "Gasoduto"
            else: objectType = "Base Terrestre"
            #else: objectType = "?"

            positions.append((objectType, info[index][2]+ info[index][4]/2, info[index][3]+info[index][5]/2))

            cv2.putText(imgContour, objectType, (info[index][2], info[index][3]+5), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0,0,0))
    
    return imgContour, positions