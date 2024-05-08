import cv2
import cv2.face
import os
import numpy as np

def checkDataset(directory='dataset/'):
    if not os.path.exists(directory) & len(os.listdir(directory)) != 0:
        return True
    return False
names = {0:'None',1:'Axel',2:'Agung'}
def organizeDataset(path='dataset/'):
  dataset_path = [os.path.join(path, f) for f in os.listdir(path)]
  faces = []
  faceID = np.array([], dtype="int")
  for i in dataset_path:
    img = cv2.cvtColor(cv2.imread(i), cv2.COLOR_BGR2GRAY)

    # Split the filename (handle potential empty elements)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    filename_parts = i.split(".")  # Split on extension
    if len(filename_parts) > 1:  # Check if there's an extension
      name_id = filename_parts[0].split("-")  # Split remaining part on delimiter
      if len(name_id) > 1:  # Check if there's a delimiter and ID part
        id = int(name_id[1])  # Extract ID (assuming it's the second element)
      else:
        # Handle case where filename doesn't follow expected format (assign default ID or log error)
        id = -1  # Example: Assign a default ID
    else:
      # Handle case where filename has no extension (assign default ID or log error)
      id = -1  # Example: Assign a default ID

    face = face_cascade.detectMultiScale(img)
    for (x, y, w, h) in face:
        faces.append(img[y:y+h, x:x+w])
        faceID = np.append(faceID,names.get(id,1))

  return faces, faceID

def trainModel(faces, faceID):
  face_recognizer = cv2.face.LBPHFaceRecognizer_create()
  face_recognizer.train(faces, faceID)
  return face_recognizer

if checkDataset():
  faces, faceID = organizeDataset()
  face_recognizer = trainModel(faces, faceID)
  face_recognizer.save('face_model.yml')
else:
  print("Dataset not found or is empty.")