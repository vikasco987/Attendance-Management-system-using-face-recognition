# import tkinter as tk
# from tkinter import *
# import os, cv2
# import shutil
# import csv
# import numpy as np
# from PIL import ImageTk, Image
# import pandas as pd
# import datetime
# import time
# import tkinter.ttk as tkk
# import tkinter.font as font

# haarcasecade_path = "haarcascade_frontalface_default.xml"
# trainimagelabel_path = (
#     "TrainingImageLabel\\Trainner.yml"
# )
# trainimage_path = "TrainingImage"
# studentdetail_path = (
#     "StudentDetails\\studentdetails.csv"
# )
# attendance_path = "Attendance"
# # for choose subject and fill attendance
# def subjectChoose(text_to_speech):
#     def FillAttendance():
#         sub = tx.get()
#         now = time.time()
#         future = now + 20
#         print(now)
#         print(future)
#         if sub == "":
#             t = "Please enter the subject name!!!"
#             text_to_speech(t)
#         else:
#             try:
#                 recognizer = cv2.face.LBPHFaceRecognizer_create()
#                 try:
#                     recognizer.read(trainimagelabel_path)
#                 except:
#                     e = "Model not found,please train model"
#                     Notifica.configure(
#                         text=e,
#                         bg="black",
#                         fg="yellow",
#                         width=33,
#                         font=("times", 15, "bold"),
#                     )
#                     Notifica.place(x=20, y=250)
#                     text_to_speech(e)
#                 facecasCade = cv2.CascadeClassifier(haarcasecade_path)
#                 df = pd.read_csv(studentdetail_path)
#                 cam = cv2.VideoCapture(0)
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 col_names = ["Enrollment", "Name"]
#                 attendance = pd.DataFrame(columns=col_names)
#                 while True:
#                     ___, im = cam.read()
#                     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#                     faces = facecasCade.detectMultiScale(gray, 1.2, 5)
#                     for (x, y, w, h) in faces:
#                         global Id

#                         Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
#                         if conf < 70:
#                             print(conf)
#                             global Subject
#                             global aa
#                             global date
#                             global timeStamp
#                             Subject = tx.get()
#                             ts = time.time()
#                             date = datetime.datetime.fromtimestamp(ts).strftime(
#                                 "%Y-%m-%d"
#                             )
#                             timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
#                                 "%H:%M:%S"
#                             )
#                             aa = df.loc[df["Enrollment"] == Id]["Name"].values
#                             global tt
#                             tt = str(Id) + "-" + aa
#                             # En='1604501160'+str(Id)
#                             attendance.loc[len(attendance)] = [
#                                 Id,
#                                 aa,
#                             ]
#                             cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
#                             cv2.putText(
#                                 im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
#                             )
#                         else:
#                             Id = "Unknown"
#                             tt = str(Id)
#                             cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
#                             cv2.putText(
#                                 im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
#                             )
#                     if time.time() > future:
#                         break

#                     attendance = attendance.drop_duplicates(
#                         ["Enrollment"], keep="first"
#                     )
#                     cv2.imshow("Filling Attendance...", im)
#                     key = cv2.waitKey(30) & 0xFF
#                     if key == 27:
#                         break

#                 ts = time.time()
#                 print(aa)
#                 # attendance["date"] = date
#                 # attendance["Attendance"] = "P"
#                 attendance[date] = 1
#                 date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
#                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
#                 Hour, Minute, Second = timeStamp.split(":")
#                 # fileName = "Attendance/" + Subject + ".csv"
#                 path = os.path.join(attendance_path, Subject)
#                 if not os.path.exists(path):
#                     os.makedirs(path)
#                 fileName = (
#                     f"{path}/"
#                     + Subject
#                     + "_"
#                     + date
#                     + "_"
#                     + Hour
#                     + "-"
#                     + Minute
#                     + "-"
#                     + Second
#                     + ".csv"
#                 )
#                 attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
#                 print(attendance)
#                 attendance.to_csv(fileName, index=False)

#                 m = "Attendance Filled Successfully of " + Subject
#                 Notifica.configure(
#                     text=m,
#                     bg="black",
#                     fg="yellow",
#                     width=33,
#                     relief=RIDGE,
#                     bd=5,
#                     font=("times", 15, "bold"),
#                 )
#                 text_to_speech(m)

#                 Notifica.place(x=20, y=250)

#                 cam.release()
#                 cv2.destroyAllWindows()

#                 import csv
#                 import tkinter

#                 root = tkinter.Tk()
#                 root.title("Attendance of " + Subject)
#                 root.configure(background="black")
#                 cs = os.path.join(path, fileName)
#                 print(cs)
#                 with open(cs, newline="") as file:
#                     reader = csv.reader(file)
#                     r = 0

#                     for col in reader:
#                         c = 0
#                         for row in col:

#                             label = tkinter.Label(
#                                 root,
#                                 width=10,
#                                 height=1,
#                                 fg="yellow",
#                                 font=("times", 15, " bold "),
#                                 bg="black",
#                                 text=row,
#                                 relief=tkinter.RIDGE,
#                             )
#                             label.grid(row=r, column=c)
#                             c += 1
#                         r += 1
#                 root.mainloop()
#                 print(attendance)
#             except:
#                 f = "No Face found for attendance"
#                 text_to_speech(f)
#                 cv2.destroyAllWindows()

#     ###windo is frame for subject chooser
#     subject = Tk()
#     # windo.iconbitmap("AMS.ico")
#     subject.title("Subject...")
#     subject.geometry("580x320")
#     subject.resizable(0, 0)
#     subject.configure(background="black")
#     # subject_logo = Image.open("UI_Image/0004.png")
#     # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
#     # subject_logo1 = ImageTk.PhotoImage(subject_logo)
#     titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
#     titl.pack(fill=X)
#     # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
#     # l1.place(x=100, y=10)
#     titl = tk.Label(
#         subject,
#         text="Enter the Subject Name",
#         bg="black",
#         fg="green",
#         font=("arial", 25),
#     )
#     titl.place(x=160, y=12)
#     Notifica = tk.Label(
#         subject,
#         text="Attendance filled Successfully",
#         bg="yellow",
#         fg="black",
#         width=33,
#         height=2,
#         font=("times", 15, "bold"),
#     )

#     def Attf():
#         sub = tx.get()
#         if sub == "":
#             t = "Please enter the subject name!!!"
#             text_to_speech(t)
#         else:
#             os.startfile(
#                 f"Attendance\\{sub}"
#             )

#     attf = tk.Button(
#         subject,
#         text="Check Sheets",
#         command=Attf,
#         bd=7,
#         font=("times new roman", 15),
#         bg="black",
#         fg="yellow",
#         height=2,
#         width=10,
#         relief=RIDGE,
#     )
#     attf.place(x=360, y=170)

#     sub = tk.Label(
#         subject,
#         text="Enter Subject",
#         width=10,
#         height=2,
#         bg="black",
#         fg="yellow",
#         bd=5,
#         relief=RIDGE,
#         font=("times new roman", 15),
#     )
#     sub.place(x=50, y=100)

#     tx = tk.Entry(
#         subject,
#         width=15,
#         bd=5,
#         bg="black",
#         fg="yellow",
#         relief=RIDGE,
#         font=("times", 30, "bold"),
#     )
#     tx.place(x=190, y=100)

#     fill_a = tk.Button(
#         subject,
#         text="Fill Attendance",
#         command=FillAttendance,
#         bd=7,
#         font=("times new roman", 15),
#         bg="black",
#         fg="yellow",
#         height=2,
#         width=12,
#         relief=RIDGE,
#     )
#     fill_a.place(x=195, y=170)
#     subject.mainloop()















import face_recognition
import cv2
import numpy as np
import pickle
import os
import pandas as pd
from datetime import datetime

# Define file paths
MODEL_PATH = "TrainedModel/encodings.pkl"
EMPLOYEE_DETAILS_PATH = "EmployeeDetails.csv"
ATTENDANCE_DIR = "Attendance"

def mark_attendance():
    """
    Captures video from the webcam, recognizes faces, and marks attendance.
    """
    # Check if the trained model exists
    if not os.path.exists(MODEL_PATH):
        print("Error: Trained model file not found. Please train the model first.")
        return

    # Load the trained model data
    with open(MODEL_PATH, "rb") as f:
        data = pickle.load(f)
    
    known_encodings = data["encodings"]
    known_ids = data["ids"]

    # Load employee details for name and department
    try:
        df_emp = pd.read_csv(EMPLOYEE_DETAILS_PATH)
    except FileNotFoundError:
        print("Error: EmployeeDetails.csv not found. Make sure it exists.")
        return

    # Create the attendance directory if it doesn't exist
    if not os.path.exists(ATTENDANCE_DIR):
        os.makedirs(ATTENDANCE_DIR)
        
    cam = cv2.VideoCapture(0)
    recognized_today = set()

    print("Starting attendance system. Press 'q' to exit.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: Failed to capture video from webcam.")
            break

        # Convert the frame to RGB for face_recognition library
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Find all faces and their encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            # Compare the face with known faces
            face_distances = face_recognition.face_distance(known_encodings, encoding)
            best_match_index = np.argmin(face_distances)
            
            # Check if the best match is within a tolerance level (e.g., a face is a match if distance is less than 0.6)
            if face_distances[best_match_index] < 0.6:
                emp_id = known_ids[best_match_index]
                
                # Get employee name for display
                emp_info = df_emp[df_emp["Emp_ID"] == int(emp_id)]
                if not emp_info.empty:
                    name = emp_info["Name"].values[0]
                    
                    # Display name and confidence on the frame
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

                    # Mark attendance if not already recorded for today
                    if emp_id not in recognized_today:
                        recognized_today.add(emp_id)
                        
                        now = datetime.now()
                        date_str = now.strftime("%Y-%m-%d")
                        time_str = now.strftime("%H:%M:%S")

                        # Prepare data for attendance record
                        emp_name = emp_info["Name"].values[0]
                        emp_dept = emp_info["Department"].values[0] if "Department" in emp_info else "N/A"
                        attendance_data = {
                            "Emp_ID": [emp_id],
                            "Name": [emp_name],
                            "Department": [emp_dept],
                            "Date": [date_str],
                            "Time": [time_str]
                        }
                        df_attendance = pd.DataFrame(attendance_data)

                        # Define the attendance file path for today
                        attendance_file = os.path.join(ATTENDANCE_DIR, f"{date_str}.csv")
                        
                        # Append to the CSV file
                        if not os.path.exists(attendance_file):
                            df_attendance.to_csv(attendance_file, index=False)
                            print(f"Attendance marked for {emp_name} ({emp_id}) at {time_str}. New file created.")
                        else:
                            df_attendance.to_csv(attendance_file, mode='a', header=False, index=False)
                            print(f"Attendance marked for {emp_name} ({emp_id}) at {time_str}. Appended to existing file.")
                else:
                    print(f"Employee with ID {emp_id} not found in EmployeeDetails.csv.")
            else:
                # If no match is found, label as 'Unknown'
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.putText(frame, "Unknown", (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

        # Display the video frame
        cv2.imshow("Office Attendance - Press Q to exit", frame)
        
        # Exit the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up resources
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    mark_attendance()