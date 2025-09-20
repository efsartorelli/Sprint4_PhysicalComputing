import cv2
import face_recognition
import serial
import time

arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

cap = cv2.VideoCapture("video.mp4")

rosto_autorizado = None
ultimo_envio = None
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo")
        break

    frame_count += 1

    # Processa só 1 em cada 5 frames
    if frame_count % 5 == 0:
        # Reduz bem a resolução para acelerar
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        acesso = False

        for face_encoding in face_encodings:
            if rosto_autorizado is None:
                rosto_autorizado = face_encoding
                acesso = True
            else:
                match = face_recognition.compare_faces([rosto_autorizado], face_encoding, tolerance=0.5)
                acesso = match[0]

        if acesso:
            texto = "Acesso Liberado"
            cor = (0, 255, 0)
            msg = b'1'
        else:
            texto = "Acesso Negado"
            cor = (0, 0, 255)
            msg = b'0'

        if msg != ultimo_envio:
            arduino.write(msg)
            ultimo_envio = msg

    # Mostra vídeo normal, mas com texto da última análise
    try:
        cv2.putText(frame, texto, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, cor, 2)
    except:
        pass

    cv2.imshow("Reconhecimento Facial", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
