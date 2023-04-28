import cv2 as cv
import mediapipe as mp
import datetime 

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
print(cap.get(3))
print(cap.get(4))


while True:
    success, frame = cap.read()
    font = cv.FONT_HERSHEY_COMPLEX_SMALL
    text = f"Width {str(cap.get(3))} Height {str(cap.get(4))}"
    # frame = cv.rectangle(frame, (0,0), (255,255), (150, 60, 150), 5) # BGR format lol
    frame = cv.putText(frame, text, (10, 50), font, 1,
                       (140, 40, 160), 2, cv.LINE_AA)
    cv.imshow("image", frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()