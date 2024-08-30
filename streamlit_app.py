import streamlit as st
import cv2
import time 
import face_recognition
if st.button("Pay"):
    cap2 = cv2.VideoCapture(0)
    result, image = cap2.read()
    cv2.imwrite("Antr.png",image)
   # time.sleep(2)2 
    cv2.destroyAllWindows()
    cap2.release()
    time.sleep(3)
    cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture("GATE.mp4")
    while True:
        result, image = cap.read()
        cv2.imwrite("Sample.png",image)
        time.sleep(2)
        picture_of_passenger = face_recognition.load_image_file("Antr.png")
        face_encodings_of_me = face_recognition.face_encodings(picture_of_passenger)
        picture_of_Rishab = face_recognition.load_image_file("unknown.jpg")
        face_encodings_of_Rishab = face_recognition.face_encodings(picture_of_Rishab)

        if not face_encodings_of_me or not face_encodings_of_Rishab:
            print("No faces found in known images")
            time.sleep(2)  
            continue
        known_face_encodings = face_encodings_of_me + face_encodings_of_Rishab
        known_face_names = ["Antriksh"] * len(face_encodings_of_me) + ["Rishab"] * len(face_encodings_of_Rishab)

        unknown_picture = face_recognition.load_image_file("Sample.png")
        face_encodings_of_unknown = face_recognition.face_encodings(unknown_picture)
        if not face_encodings_of_unknown:
            print("No faces found in unknown image")
            time.sleep(2)  
            continue

        for unknown_face_encoding in face_encodings_of_unknown:
            results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, unknown_face_encoding)

            best_match_index = face_distances.argmin()
            name = known_face_names[best_match_index]
            if results[best_match_index]:
                print(f"This is the known person")
                while(cap1.isOpened()):
                    ret,frame = cap1.read()
                    cv2.imshow("video", frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
            else:
                print("NO FACE")

