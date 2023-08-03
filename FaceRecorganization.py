import face_recognition
import cv2
import numpy as np 
import csv
from datetime import datetime


video_capture = cv2.VideoCapture(0)

#Load known faces
Rajeshwar_image = face_recognition.load_image_file("Faces.jpeg")
Rajeshwar_Encoding = face_recognition.face_encoding(Rajeshwar_image)[0]

known_face_encoding = [Rajeshwar_Encoding]
known_face_name = ["Rajeshwar"]

#List of expected students
students = known_face_name.copy()

face_loacations = []
face_encodings = []

#Get the current date and time 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

#Writing the date in attendance file 
f = open(f"{current_date}.csv","w+",newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

    #Recognize faces
    face_loacations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame)


    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
        face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
        best_match_index = np.argmin(face_distance)
        
        if (matches[best_match_index] ):
            name = known_face_name[best_match_index]
    
    cv2.imshow("Attendance",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    #Add the text if person is present 
    if name in known_face_name:
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10,100)
        fontScale = 1.5
        fontColor = (255, 0, 0)
        thickness = 3
        lineType = 2
        cv2.putText(frame, name+"Present",bottomLeftCornerOfText,font,fontScale,fontColor,thickness,lineType)

        if name in students: 
            students.remove(name)
            current_Time = now.strftime("%H-%M-%S")
            lnwriter.writerow([name,current_Time]) 
video_capture.release()
cv2.destroyAllWindows()
f.close()