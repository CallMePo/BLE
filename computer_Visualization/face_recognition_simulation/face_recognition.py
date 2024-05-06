import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_model.yml')
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0
names = ['None','Axel']
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        if confidence < 100:
            id = names[id]
        else:
            id = "unknown"
            confidence = "  {}%".format(round(100 - confidence))
        cv2.putText(frame, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(frame, str(confidence), (x+5, y+h-5), font, 1, (255, 255, 0), 1)
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()