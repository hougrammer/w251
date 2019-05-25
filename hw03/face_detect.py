from __future__ import print_function
import numpy as np
import cv2
import paho.mqtt.client as mqtt
import base64

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

client = mqtt.Client()
client.connect('face_detector')

i = 0 # frame index
while(True): 
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)
        r = max(w, h) / 2
        centerx = x + w / 2
        centery = y + h / 2
        nx = int(centerx - r)
        ny = int(centery - r)
        nr = int(r * 2)

        faceimg = frame[ny:ny+nr, nx:nx+nr]
        lastimg = cv2.resize(faceimg, (256, 256))
        
        if i % 60 == 0:
            print('Publishing frame {} to MQTT broker'.format(i))
            cv2.imwrite('image.jpg', lastimg)
            with open('image.jpg', 'rb') as f:
                client.publish('detector_out',  base64.b64encode(f.read()))

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    i += 1

cap.release()
cv2.destroyAllWindows()
client.disconnect()
