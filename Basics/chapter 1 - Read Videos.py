import cv2

#                                  Video Read

cap = cv2.VideoCapture("./test-resources/boys.mp4") # Reading the video (PATH), it's a sequence of images/frames

while True: # Loop to keep going to go through the frames of the video
    success, frameImg = cap.read() # Read each frame

    try:
        cv2.imshow("Test Window", frameImg)
        key = cv2.waitKey(5) # Key to close the video window
        if key == 27: # 27 = ESC
            print("Closing the window...")
            break
    except: # If the video ends it will show an error, that can be avoided using the success variable or the try/except method
        print("The video ended...")
        print("Closing the window...")
        break

cv2.destroyAllWindows() # Close all the windows if needed
