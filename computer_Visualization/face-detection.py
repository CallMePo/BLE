import cv2

cascade_path = 'haarcascade_frontalface_default.xml'
clf = cv2.CascadeClassifier(cascade_path)

camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(gray, 1.1, 5, flags=cv2.CASCADE_SCALE_IMAGE, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()