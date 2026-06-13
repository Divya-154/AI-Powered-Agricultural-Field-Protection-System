from ultralytics import YOLO
import cv2
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

allowed_animals = [
    "dog",
    "cat",
    "cow",
    "horse",
    "sheep",
    "bird"
]

print("Smart Farm Protection System Started...")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    animal_detected = False

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])
            name = model.names[cls]

            if name in allowed_animals:
                animal_detected = True
                print(f"{name} detected")

    if animal_detected:
        ser.write(b'1')
    else:
        ser.write(b'0')

    annotated_frame = results[0].plot()

    cv2.imshow("Smart Farm Protection System", annotated_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
