import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
dataset_path='dataset/'

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

person_id = 1
count = 0
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5, minSize=(30, 30))

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