import cv2

"""

#                                   Img Read

img = cv2.imread("./test-resources/street.jpg") # Reading the image (PATH)

print(img) # Real structure of the image

cv2.imshow("Test Window", img) # Displaying the image (Name of the window, image variant)
cv2.waitKey(0) # To not instantly close the Image window, (0 or milisseconds) - 0 is infinit, milisseconds is the time until it go ahead in the coad

"""

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

"""

#                                WebCam Read

webcam = cv2.VideoCapture(0) # Default webcam id, but if you have more than one you can choose
# Things you can set
webcam.set(3, width)
webcam.set(4, height)
webcam.set(10, brightness)
...
0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
5. CV_CAP_PROP_FPS Frame rate.
6. CV_CAP_PROP_FOURCC 4-character code of codec.
7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)

# The rest of the code is the same of the Video Read (in the basic example you can see a full program to that)

"""
