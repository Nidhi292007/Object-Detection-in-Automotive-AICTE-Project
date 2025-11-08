from ultralytics import YOLO
import cv2

def detect_emergency_vehicle(frame, model):
    results = model.predict(frame, conf=0.5, verbose=False)
    detected = False

    for box in results[0].boxes:
        cls_name = results[0].names[int(box.cls)]
        if cls_name.lower() in ['ambulance', 'firetruck', 'police']:
            detected = True
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.putText(frame, f"Emergency: {cls_name}", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return frame, detected

