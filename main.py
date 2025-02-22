# Full Project Code Mail : vatshayan007@gmail.com
# If you get error then Mail : vatshayan007@gmail.com
import cv2
import numpy as np
import face_recognition

imgModi = face_recognition.load_image_file('Images_Attendance/vnkt.jpg') #add u r own images in images _Attendance folder
imgModi = cv2.cvtColor(imgModi, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Images_Attendance/vnkt2.jpg') #add u r own images in images _Attendance folder for checking vnkt vnkt1 both are same or not 
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgModi)[0]
encodeModi = face_recognition.face_encodings(imgModi)[0]
cv2.rectangle(imgModi, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (155, 0, 255), 2)

facelocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (facelocTest[3], facelocTest[0]), (facelocTest[1], facelocTest[2]), (155, 0, 255), 2)

results = face_recognition.compare_faces([encodeModi], encodeTest)
faceDis = face_recognition.face_distance([encodeModi], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)

cv2.imshow('modi', imgModi)
cv2.imshow('narendra-modi', imgTest)
cv2.waitKey(0)
