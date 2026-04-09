import cv2
import time
from detector import VehicleDetector
from traffic_analyzer import TrafficAnalyzer
from predictor import TrafficPredictor
from utils import Visualizer

def run_simulation(video_path):
    # Initialize components
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Get frame properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Initialize detector, analyzer, predictor, and visualizer
    detector = VehicleDetector()
    analyzer = TrafficAnalyzer(frame_width)
    predictor = TrafficPredictor()
    visualizer = Visualizer()
    
    actual_counts = []
    predicted_counts = []
    
    print("Simulation started. Press 'q' to exit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # 1. Detect vehicles
        detections, is_emergency = detector.detect_vehicles(frame)
        total_vehicles = len(detections)
        
        # 2. Analyze lane-wise counts
        lane_counts = analyzer.analyze_lanes(detections)
        
        # 3. Classify traffic density and signal timing
        density, signal_time = analyzer.get_density_info(total_vehicles, is_emergency)
        
        # 4. Predict future traffic
        prediction = predictor.predict_next(total_vehicles)
        
        # 5. Store counts for later graphing
        actual_counts.append(total_vehicles)
        predicted_counts.append(prediction)
        
        # 6. Prepare visualization stats
        stats = {
            'total': total_vehicles,
            'lane_counts': lane_counts,
            'density': density,
            'signal_time': signal_time,
            'prediction': prediction
        }
        
        # 7. Render visualization
        visualizer.draw_detections(frame, detections, analyzer.lane_width)
        visualizer.draw_info_panel(frame, stats)
        
        # 8. Display output
        cv2.imshow('IntelliSignal: AI Traffic Control System', frame)
        
        # Stop simulation if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up and plot results
    cap.release()
    cv2.destroyAllWindows()
    
    print("Simulation ended. Plotting results...")
    visualizer.plot_traffic_stats(actual_counts, predicted_counts)

if __name__ == "__main__":
    # Ensure traffic.mp4 exists in the directory
    run_simulation(r"C:\Users\my pc\OneDrive\Documents\fods\IntelliSignal\WhatsApp Video 2026-03-18 at 10.30.40.mp4")
