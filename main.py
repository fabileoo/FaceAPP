import tkinter as tk
from tkinter import filedialog, messagebox
import face_recognition
import numpy as np
import os

# dir with faces
KNOW_FACES_DIR ="know_faces"

know_faces_encodings= {}
for person_name in os.listdir(KNOW_FACES_DIR):
    person_dir = os.path.join(KNOW_FACES_DIR, person_name)
    if os.path.isdir(person_dir):
        know_faces_encodings[person_name]=[]
        for filename in os.listdir(person_dir):
            if filename.endswith((".jpg",".png")):
                path = os.path.join(person_dir,filename)
                image =face_recognition.load_image_file(path)
                encodings =face_recognition.face_encodings(image)
                if encodings:
                    know_faces_encodings[person_name].append(encodings[0])

#function for detect face
def recognize_face(photo_path):
    image =face_recognition.load_image_file(photo_path)
    encodings= face_recognition.face_encodings(image)

    if not encodings:
        return "Face not found"
    
    for face_encoding in encodings:
        for name, face_list in know_faces_encodings.items():
            results = face_recognition.compare_faces(face_list,face_encoding)
            if True in results:
                return name
    return "Unknown person"

#work
photo_to_check = "test4.jpg"
result = recognize_face(photo_to_check)
print(f"On photo: {result}")
    