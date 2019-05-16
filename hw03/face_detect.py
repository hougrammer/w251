import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(gray, (x,y), (x+w,y+h), (255,0,0), 2)

    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
#cv.destroyAllWindows()
