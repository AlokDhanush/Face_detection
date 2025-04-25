import cv2 
import numpy as np 

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "my_image1.png"
        
        cv2.imwrite(img_item, roi_gray) 

        color = (0, 0, 255) 
        stroke = 2
        end_x = x + w
        end_y = y + h 
        cv2.rectangle(frame, (x, y), (end_x, end_y), color, stroke)

    mirror_frame = cv2.flip(frame, 1)
    cv2.imshow("Frame", mirror_frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()
