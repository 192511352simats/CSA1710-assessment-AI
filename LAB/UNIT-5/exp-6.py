import face_recognition

known = face_recognition.load_image_file(input("Enter known image: "))
test = face_recognition.load_image_file(input("Enter test image: "))

k = face_recognition.face_encodings(known)[0]
t = face_recognition.face_encodings(test)[0]

result = face_recognition.compare_faces([k], t)

print("Face Recognized!" if result[0] else "Face Not Recognized!")
