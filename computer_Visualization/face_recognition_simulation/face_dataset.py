import cv2
import os
import urllib.request

cascade_file = 'haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_file):
    url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
    urllib.request.urlretrieve(url, cascade_file)

face_cascade = cv2.CascadeClassifier(cascade_file)
cap = cv2.VideoCapture(0)
dataset_path='dataset/'

if not os.path.exists(dataset_path):
    os.mkdir(dataset_path)

person_id = 2 #change this to your own ID
count = 0
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    faces = face_cascade.detectMultiScale(frame, 1.1, 5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        count += 1
        cv2.imwrite(dataset_path + "person_" + str(person_id) + "_" + str(count) + ".jpg", gray[y:y+h, x:x+w])

    cv2.imshow('camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif count == 30:
        break
cap.release()
cv2.destroyAllWindows()