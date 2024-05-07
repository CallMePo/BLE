import cv2
import os
import numpy as np

def checkDataset(directory='dataset/'):
    if not os.path.exists(directory) & len(os.listdir(directory)) != 0:
        return True
    return False

def organizeDataset(path='dataset/'):
    dataset_path = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    faceID = np.array([], dtype="int")
    for i in dataset_path:
        img = cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2GRAY)
        id = int(i.split()[-1].split('.')[0].split('-')[1])
        face = face_cascade.detectMultiScale(img)
        for (x, y, w, h) in face:
            faces.append(img[y:y+h, x:x+w])
            faceID = np.append(faceID,id)
    return faces, faceID
if not checkDataset():
    print("Dataset is empty. Please run face_dataset.py to create dataset.")
else:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #train
    print("Training...")
    try:
        result = organizeDataset()
        print(result)
        faces, faceID = result
    except Exception as e:
        print(e)
    print("Training finished.")

    #save model
    recognizer.write('face_model.yml')
    print("Model saved.")