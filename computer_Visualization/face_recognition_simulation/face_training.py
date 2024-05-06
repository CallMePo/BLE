import cv2
import os
import numpy as np

def checkDataset():
    if not os.path.exists('dataset/') & len(os.listdir('dataset/')) != 0:
        return True
    return False

def organizeDataset():
    faces = []
    faceID = np.array([], dtype="int")
    dataset_path = [os.path.join('dataset/', f) for f in os.listdir('dataset/')]
    for i in dataset_path:
        img = cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(i)[-1].split('.')[0].split('-')[1])
        face = face_cascade.detectMultiScale(img)
        for (x, y, w, h) in face:
            faces.append(img[y:y+h, x:x+w])
            faceID.append(id)
    return faces, faceID
if not checkDataset():
    print("Dataset is empty. Please run face_dataset.py to create dataset.")
else:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #train
    print("Training...")
    faces, faceID = organizeDataset()
    recognizer.train(faces, np.array(faceID))
    print("Training finished.")

    #save model
    recognizer.save('face_model.yml')
    print("Model saved.")