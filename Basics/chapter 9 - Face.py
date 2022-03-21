import cv2
from functions import stack

# Using "Viola & Jones" method
# And to that it's needed to use AI and train the model, but to save time, we're going to use downloaded AI (.xml files from OpenCV cascades)

img = cv2.imread("test-resources/faces.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting Faces
faceAI = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml") # model
faces = faceAI.detectMultiScale(imgGray, 1.1, 4) # (img, ...parameters that I don't know)

# Putting in the Image
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) # Green rectangle in the faces

imgStack = stack.join([[img]])

cv2.imshow("Images", imgStack)

cv2.waitKey(0)