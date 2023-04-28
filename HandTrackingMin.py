import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)


while True:
    success, frame = cap.read()

    cv.imshow("image", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()