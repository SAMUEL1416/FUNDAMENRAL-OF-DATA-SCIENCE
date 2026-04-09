import cv2
import asyncio
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, StreamingResponse
from detector import VehicleDetector
from traffic_analyzer import TrafficAnalyzer
from predictor import TrafficPredictor
from utils import Visualizer
import uvicorn
import json

app = FastAPI()

# Configuration
# Note: Using the specific video path provided by the user
VIDEO_PATH = r"C:\Users\my pc\OneDrive\Documents\fods\IntelliSignal\WhatsApp Video 2026-03-18 at 10.30.40.mp4"

# Shared Global State for Statistics
current_stats = {
    "total": 0,
    "lane_counts": [0, 0, 0],
    "density": "LOW",
    "signal_time": 20,
    "priority_lane": "All",
    "prediction": 0.0,
    "system_log": "Initializing Next-Gen Control..."
}

def generate_frames():
    global current_stats
    
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    detector = VehicleDetector()
    analyzer = TrafficAnalyzer(frame_width)
    predictor = TrafficPredictor()
    visualizer = Visualizer()

    while True:
        success, frame = cap.read()
        if not success:
            # Restart video if it ends for continuous demo
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # 1. Detect & Analyze
        detections, is_emergency = detector.detect_vehicles(frame)
        total_vehicles = len(detections)
        lane_counts = analyzer.analyze_lanes(detections)
        
        # Calculate prediction BEFORE using it for timing
        prediction = predictor.predict_next(total_vehicles)
        
        # New: Proactive Control Logic
        # We use the higher value between current count and prediction 
        # to anticipate upcoming congestion.
        effective_count_for_timing = max(total_vehicles, int(prediction))
        
        # Get density info using specific lane counts and proactive metrics
        density, signal_time, priority_lane = analyzer.get_density_info(lane_counts, is_emergency)
        
        # Provide a descriptive log for the web console
        system_log = f"Proactive Mode: Analyzing {effective_count_for_timing} vehicles. Priority set to {priority_lane}."
        if is_emergency:
            system_log = "EMERGENCY OVERRIDE: Hospital/Emergency vehicle detected. Clearing all lanes."

        # 2. Update Web Stats
        current_stats = {
            "total": total_vehicles,
            "lane_counts": lane_counts,
            "density": density,
            "signal_time": signal_time,
            "priority_lane": priority_lane,
            "prediction": prediction,
            "system_log": system_log
        }

        # 3. Draw Detections on Frame
        visualizer.draw_detections(frame, detections, analyzer.lane_width)
        
        # 4. Encode frame for transmission
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.get('/')
def index():
    """Serves the main dashboard page."""
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return HTMLResponse(content)

@app.get('/video_feed')
def video_feed():
    """Streams the processed video frames."""
    return StreamingResponse(generate_frames(), 
                             media_type='multipart/x-mixed-replace; boundary=frame')

@app.get('/stats')
def get_stats():
    """Returns the latest traffic analytics."""
    return current_stats

if __name__ == "__main__":
    # Start the server
    print("IntelliSignal Web Console running at http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
