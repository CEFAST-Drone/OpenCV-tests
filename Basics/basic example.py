import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validaçao, frame = webcam.read()
    while validaçao:
        validaçao, frame = webcam.read()
        cv2.imshow("Minha Webcam", frame)
        key = cv2.waitKey(5)
        if key == 27:
            break
    cv2.imwrite("Minhafoto.png", frame)

webcam.release()
cv2.destroyAllWindows()
