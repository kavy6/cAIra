# Face Emotion Detection

import cv2
import numpy as np
from deepface import DeepFace

# Webcam
cam = cv2.VideoCapture(0)
face_detected = False

while(True):
    ret, frame = cam.read()
    cv2.imshow("Live", frame)
    
    # Face detection logic    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale (gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , 3)
    
    
    # Emotion detection logic
    try:
        predictions = DeepFace.analyze(frame)

        emotion = predictions["dominant_emotion"]
        gender = predictions["gender"]

        frame = cv2.putText(frame, emotion, (100,120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, str(gender), (100,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
        
        
    except:
        print("no face detected")
        
    cv2.imshow("Live", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        f = open("data.txt", "a")
        f.write(" ")
        f.write(emotion)
        f.write(" ")
        f.close()
        break

    
        
cam.release()
cv2.destroyAllWindows()

import chatbot
