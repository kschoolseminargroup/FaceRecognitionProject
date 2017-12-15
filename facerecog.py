import face_recognition
import cv2

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
my_image = face_recognition.load_image_file("keonhee.jpg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]

junho_image = face_recognition.load_image_file("junho.jpg")
junho_face_encoding = face_recognition.face_encodings(junho_image)[0]

namwoo_image = face_recognition.load_image_file("namwoo.jpg")
namwoo_face_encoding = face_recognition.face_encodings(namwoo_image)[0]

natasha_image = face_recognition.load_image_file("1.jpg")
natasha_face_encoding = face_recognition.face_encodings(natasha_image)[0]

prof_image = face_recognition.load_image_file("2.jpg")
prof_face_encoding = face_recognition.face_encodings(prof_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([my_face_encoding, junho_face_encoding, namwoo_face_encoding, natasha_face_encoding, prof_face_encoding], face_encoding, tolerance = 0.4)
            name = "UNKNOWN"


            if match[0]:
                name = "Keonhee"

            if match[1]:
            	name = "Junho"

            if match[2]:
            	name = "Namwoo"

            if match[3] :
            	name = "Natasha Ivanokov"

            if match[4] :
            	name = "Jo Sungho"



            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
