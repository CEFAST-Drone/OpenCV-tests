import cv2
from functions import stack

# Joining

imgs = ['img1', 'img2', 'img3', 'img4']

for index, imgPath in enumerate(imgs): # Reading images
    imgs[index] = cv2.imread(imgPath)

fullImage = stack.join([
        [img[0], img[1]],
        [img[2], img[3]]
                ])

cv2.imshow("Full Image", fullImage)

cv2.waitKey(0)