import tkinter as tk
from tkinter import filedialog, messagebox
import face_recognition
import numpy as np
import os
import cv2

# dir with faces
KNOWN_FACES_DIR ="know_faces"

known_face_encodings = []
known_face_names = []

# === ЗАГРУЗКА И КОДИРОВАНИЕ ИЗОБРАЖЕНИЙ ===
for name in os.listdir(KNOWN_FACES_DIR):
    person_dir = os.path.join(KNOWN_FACES_DIR, name)
    if not os.path.isdir(person_dir):
        continue

    for file in os.listdir(person_dir):
        if file.lower().endswith((".jpg", ".png")):
            path = os.path.join(person_dir, file)
            image = face_recognition.load_image_file(path)

            encs = face_recognition.face_encodings(image)
            if len(encs) == 0:
                print(f"Лицо не найдено: {path}")
                continue

            known_face_encodings.append(encs[0])
            known_face_names.append(name)

print("Известных лиц загружено:", len(known_face_names))

# === КАМЕРА ===
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)

    if face_locations:
        face_encodings = face_recognition.face_encodings(
            rgb, known_face_locations=face_locations, num_jitters=0
        )

        for encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            name = "Unknown"

            distances = face_recognition.face_distance(
                known_face_encodings, encoding
            )

            if len(distances) > 0:
                best = np.argmin(distances)
                if distances[best] < 0.5:
                    name = known_face_names[best]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(
                frame,
                name,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# known_faces_encodings= {}
# for person_name in os.listdir(KNOWn_FACES_DIR):
#     person_dir = os.path.join(KNOWn_FACES_DIR, person_name)
#     if os.path.isdir(person_dir):
#         known_faces_encodings[person_name]=[]
#         for filename in os.listdir(person_dir):
#             if filename.endswith((".jpg",".png")):
#                 path = os.path.join(person_dir,filename)
#                 image =face_recognition.load_image_file(path)
#                 encodings =face_recognition.face_encodings(image)
#                 if encodings:
#                     known_faces_encodings[person_name].append(encodings[0])

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         continue

#     rgb_frame = frame[:, :, ::-1]

#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#     for face_encoding, face_location in zip(face_encodings, face_locations):
#         name = "Unknown"
#         for person_name, face_list in know_faces_encodings.items():
#             results = face_recognition.compare_faces(face_list, face_encoding)
#             if True in results:
#                 name = person_name
#                 break

#         top, right, bottom, left = face_location
#         cv2.rectangle(frame, (left,top),(right,bottom),(0,255,0),2)
#         cv2.putText(frame,name, (left,top - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,255,0),2)

#         if name != "Unknown":
#             print(f"Access granted for {name}")
    
#     cv2.imshow("Face Recognition", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
    
#function for detect face
# def recognize_face(photo_path):
#     image =face_recognition.load_image_file(photo_path)
#     encodings= face_recognition.face_encodings(image)

#     if not encodings:
#         return "Face not found"
    
#     for face_encoding in encodings:
#         for name, face_list in know_faces_encodings.items():
#             results = face_recognition.compare_faces(face_list,face_encoding)
#             if True in results:
#                 return name
#     return "Unknown person"

# #work
# photo_to_check = "test4.jpg"
# result = recognize_face(photo_to_check)
# print(f"On photo: {result}")
    