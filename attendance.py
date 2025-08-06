import cv2
import numpy as np
import pandas as pd
import datetime
import os

# Create Attendance folder if not exists
if not os.path.exists('Attendance'):
    os.makedirs('Attendance')

# Load Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load pre-trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('TrainingImageLabel\trainer.yml')

# Load student names from CSV
def get_name_from_id(id):
    try:
        df = pd.read_csv('StudentDetails.csv')
        name_row = df[df['Id'] == id]
        if not name_row.empty:
            return name_row.iloc[0]['Name']
        else:
            return "Unknown"
    except:
        return "Unknown"

# Mark attendance
def mark_attendance(name, id):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.datetime.now().strftime("%H:%M:%S")
    filename = f'Attendance/Attendance_{date_str}.csv'

    # Create new file with headers if it doesn't exist
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("Id,Name,Date,Time\n")

    # Check if already marked
    df = pd.read_csv(filename)
    if not ((df['Id'] == id) & (df['Date'] == date_str)).any():
        with open(filename, 'a') as f:
            f.write(f"{id},{name},{date_str},{time_str}\n")

# Start webcam
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        id, confidence = recognizer.predict(face)

        if confidence < 60:
            name = get_name_from_id(id)
            mark_attendance(name, id)
            label = f"{name} ({round(100 - confidence)}%)"
        else:
            label = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y - 10), font, 0.8, (255, 255, 255), 2)

    cv2.imshow('Face Recognition Attendance', frame)

    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
