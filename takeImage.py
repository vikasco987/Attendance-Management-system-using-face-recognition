import cv2
import os
import csv
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from datetime import datetime

def take_image():
    # Create dataset directory if it doesn't exist
    path = "TrainingImage"
    if not os.path.exists(path):
        os.makedirs(path)

    # Ask for ID and Name via dialog
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    id_input = simpledialog.askstring("Input", "Enter ID:")
    name_input = simpledialog.askstring("Input", "Enter Name:")

    if not id_input or not name_input:
        messagebox.showerror("Error", "ID and Name are required!")
        return

    # Initialize camera
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    sample_num = 0

    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to open camera. Exiting.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            sample_num += 1
            face_img = gray[y:y+h, x:x+w]

            # Save the image
            file_path = os.path.join(path, f"{name_input}.{id_input}.{sample_num}.jpg")
            cv2.imwrite(file_path, face_img)

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('Face Capturing', img)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif sample_num >= 60:
            break

    cam.release()
    cv2.destroyAllWindows()

    # Save user info to CSV
    row = [id_input, name_input]
    with open('StudentDetails.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)

    print(f"Images saved for ID: {id_input}, Name: {name_input}")

if __name__ == '__main__':
    take_image()
