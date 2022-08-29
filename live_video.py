# Live Video

import tkinter as tk
from PIL import ImageTk, Image
import cv2
import numpy as np
import face_recognition

 
root = tk.Tk()

# make video window
root.title("Live Video")
root['bg'] = "#1D5A5F"

# change window icon
root.iconbitmap('C:/Users/DELL/OneDrive/Desktop/Project/icon-Copy1.ico')

# resizing the window 
root.geometry('1150x550+50+50')



#face recognition
def face_rec():
   vid = cv2.VideoCapture(0)

   #face recognition set up 
   face_1 = face_recognition.load_image_file("kavyaphoto.jpeg")
   face_1_encoding = face_recognition.face_encodings(face_1)[0]

   known_face_encodings = [face_1_encoding]
   known_face_names = ["Kavya"]


   name = "Unknown"

   while(True):

       ret, frame = vid.read()

       #face detection
       face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
       gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray, 1.3, 5)

       
        #face recognition
       face_locations = face_recognition.face_locations(frame)
       face_encodings = face_recognition.face_encodings(frame, face_locations)
       
       for (top,right, bottom, left), face_encoding in zip(face_locations, face_encodings):
           matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
           name = "Unknown"
           face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
           best_match_index = np.argmin(face_distances)
           if matches[best_match_index]:
               name = known_face_names[best_match_index]
           for (x,y,w,h) in faces:
               cv2.rectangle(frame , (x,y) , (x+w,y+h) , (0,255,0) , 3)
           
           cv2.putText(frame,name, (left, top+20), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1, cv2.LINE_AA)
       
       
       cv2.imshow("Face Recognition",frame)
       
       

       #authentication
       if name != "Unknown":
           if cv2.waitKey(1) & 0xFF == ord('q'):
               vid.release()
               cv2.destroyAllWindows()           
               break
           
       elif name == "Unknown":
           if cv2.waitKey(1) & 0xFF == ord('q'):
               vid.release()
               cv2.destroyAllWindows()
               break


   vid.release()
   cv2.destroyAllWindows()
   return name

name = face_rec()
if name == "Unknown":
   name = "Guest"
   
text = "Hi,",name


f = open("data.txt", "a")
f.write(name)
f.close()

canvas = tk.Canvas(root, width = 1000, height = 500, bg = "#1D5A5F")
canvas["highlightthickness"] = 0
canvas.pack()
canvas.create_text(200, 200, font=('Helvetica', 50), text=text, fill = "#FFC300")



# Next button
def next():
   #cap.release()
   cv2.destroyAllWindows
   root.destroy()
   
   import face_emotion

next_btn = tk.Button(root, text = "Next", bg = "#FFC300", command = next, activeforeground = "green",activebackground = "pink",pady=10, padx=50).place(x=1100, y=550)




root.mainloop()









