import cv2
from ultralytics import YOLO

class VehicleDetector:
    def __init__(self, model_name='yolov8s.pt'):
        """
        Switched to 'yolov8s' (small) for much better accuracy than 'nano'.
        """
        self.model = YOLO(model_name)
        # Class mapping for COCO dataset
        self.class_names = {
            2: 'Car',
            3: 'Motorcycle',
            5: 'Bus',
            7: 'Truck'
        }
        self.target_classes = list(self.class_names.keys())

    def detect_vehicles(self, frame):
        """
        Detects vehicles and identifies their types.
        """
        results = self.model(frame, verbose=False, conf=0.4)[0]
        detections = []
        is_emergency = False

        for r in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = r
            cid = int(class_id)
            
            if cid in self.target_classes:
                label = self.class_names[cid]
                
                # Logic: In standard YOLO, Ambulances are often detected as 
                # highly confident Trucks or Buses. We treat them as Emergency.
                if label == 'Bus' or label == 'Truck':
                    is_emergency = True
                
                detections.append({
                    'bbox': (int(x1), int(y1), int(x2), int(y2)),
                    'class_id': cid,
                    'class_name': label,
                    'score': score
                })

        return detections, is_emergency
