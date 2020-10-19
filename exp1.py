import cv2
import numpy as np
import face_recognition
import os


path = 'C:\\Users\\rajes\\Documents\\python\\pic'
images = []
classNmaes = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curImage = cv2.imread('f{path}/{cl}')
    images.append(curImage)
    classNmaes.append(os.path.splitext(cl)[0])
print(classNmaes)
def findEncoding(images):
    print(str(images))
    encodeList = []
    for img in images:
        print(img)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncoding(images)
print("encoding complete")
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    faceCurrFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurrFrame)

    for encodeface,faceloc in zip(encodeCurFrame,faceCurrFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeface)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeface)
        print(faceDis)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break