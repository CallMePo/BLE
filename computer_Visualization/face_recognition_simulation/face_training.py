import cv2
import cv2.face
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

    # Split the filename (handle potential empty elements)
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
      faceID = np.append(faceID,id)
  return faces, faceID

if not checkDataset():
    print("Dataset is empty. Please run face_dataset.py to create dataset.")
else:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #train
    print("Training...")
    faces, faceID = organizeDataset()
    recognizer.train(faces, faceID)
    print("Training finished.")

    #save model
    recognizer.write('face_model.yml')
    print("Model saved.")