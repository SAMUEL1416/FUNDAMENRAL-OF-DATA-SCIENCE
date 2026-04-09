# IntelliSignal: Next-Gen Adaptive Traffic Control System

IntelliSignal is a state-of-the-art, data-driven solution for modern urban traffic management. By leveraging computer vision and proactive predictive models, it transforms traditional intersections into intelligent, adaptive nodes in a Smart City infrastructure.

## Key Features

- **Proactive Signal Control**: Anticipates traffic spikes using a Moving Average prediction model.
- **AI-Powered Vision**: Real-time vehicle detection and classification (Cars, Bikes, buses, Trucks) using YOLOv8.
- **Lane-wise Adaptive Logic**: Dynamically allocates signal timing based on individual lane density.
- **Emergency Priority System**: Automatic high-priority clearance for ambulances and emergency vehicles.
- **Smart City Dashboard**: Professional command center interface with real-time telemetry and system diagnostics.

## Architecture

1. **Vision Engine (`detector.py`)**: High-accuracy object detection.
2. **Traffic Brain (`traffic_analyzer.py`)**: Lane analysis and density classification.
3. **Forecasting Module (`predictor.py`)**: Predictive modeling for future flow.
4. **Command Center (`app.py` & `index.html`)**: FastAPI-based web infrastructure.

## Requirements

- Python 3.8+
- OpenCV
- Ultralytics (YOLOv8)
- FastAPI & Uvicorn
- Matplotlib

## Execution

```bash
pip install -r requirements.txt
python app.py
```

Access the dashboard at `http://localhost:8000`.
