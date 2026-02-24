from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open camera
cap = cv2.VideoCapture(0)

# Virtual signal line (Y-axis)
SIGNAL_LINE_Y = 300

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    vehicle_count = 0
    violation = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # COCO classes:
            # 2 = car, 3 = motorcycle, 5 = bus, 7 = truck
            if cls in [2, 3, 5, 7]:
                vehicle_count += 1

                # Draw bounding box
                cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)

                # 🚨 Signal Jump Logic
                if y2 > SIGNAL_LINE_Y:
                    violation = True
                    cv2.putText(frame, "SIGNAL JUMP!",
                                (x1, y1-10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (0,0,255), 2)

    # Draw signal line
    cv2.line(frame, (0, SIGNAL_LINE_Y),
             (frame.shape[1], SIGNAL_LINE_Y),
             (0,0,255), 2)

    # 🚦 Traffic Status
    if vehicle_count <= 5:
        status = "NORMAL TRAFFIC"
        color = (0,255,0)
    elif vehicle_count <= 10:
        status = "HEAVY TRAFFIC"
        color = (0,255,255)
    else:
        status = "TRAFFIC JAM"
        color = (0,0,255)
        violation = True

    cv2.putText(frame, f"Vehicles: {vehicle_count}",
                (20,40), cv2.FONT_HERSHEY_SIMPLEX,
                1, color, 2)

    cv2.putText(frame, f"Status: {status}",
                (20,80), cv2.FONT_HERSHEY_SIMPLEX,
                1, color, 2)

    if violation:
        cv2.putText(frame, "TRAFFIC VIOLATION DETECTED!",
                    (20,130),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,0,255), 3)

    cv2.imshow("AI Traffic Violation System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()