import cv2
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self):
        # Color codes for visualization (BGR)
        self.colors = {
            'LOW': (0, 255, 0),        # Green
            'MEDIUM': (0, 255, 255),    # Yellow
            'HIGH': (0, 0, 255),       # Red
            'EMERGENCY': (255, 0, 0)   # Blue
        }

    def draw_detections(self, frame, detections, lane_width):
        """
        Draws bounding boxes, labels, and lane dividers.
        """
        for d in detections:
            x1, y1, x2, y2 = d['bbox']
            label = f"{d['class_name']}: {d['score']:.2f}"
            
            # Using specific colors for the boxes
            color = (255, 255, 0) # Cyan-ish
            if d['class_name'] in ['Bus', 'Truck']:
                color = (0, 0, 255) # Red for potential emergency/heavy vehicles

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Draw lane dividers (vertical lines)
        cv2.line(frame, (lane_width, 0), (lane_width, frame.shape[0]), (255, 255, 255), 2)
        cv2.line(frame, (2 * lane_width, 0), (2 * lane_width, frame.shape[0]), (255, 255, 255), 2)

    def draw_info_panel(self, frame, stats):
        """
        Displays statistics, density, signal control, and predictions on the frame.
        """
        # Define panel layout
        y_offset = 30
        x_offset = 10
        font_scale = 0.7
        color = (255, 255, 255)
        
        infos = [
            f"Total Vehicles: {stats['total']}",
            f"Lane 1: {stats['lane_counts'][0]} | Lane 2: {stats['lane_counts'][1]} | Lane 3: {stats['lane_counts'][2]}",
            f"Traffic: {stats['density']}",
            f"Signal Timing: {stats['signal_time']}s",
            f"Predicted Next: {stats['prediction']:.2f}"
        ]

        if stats['density'] == "EMERGENCY":
            cv2.putText(frame, "EMERGENCY VEHICLE DETECTED", (frame.shape[1]//2 - 150, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

        for info in infos:
            cv2.putText(frame, info, (x_offset, y_offset), 
                        cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, 2)
            y_offset += 30

    def plot_traffic_stats(self, actual_counts, predicted_counts):
        """
        Plots a graph of actual vs predicted traffic density.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(actual_counts, label='Actual Vehicles', color='blue', linestyle='--')
        plt.plot(predicted_counts, label='Predicted Vehicles', color='orange')
        plt.title('IntelliSignal: Traffic Density Analysis & Prediction')
        plt.xlabel('Time (Frames)')
        plt.ylabel('Vehicle Count')
        plt.legend()
        plt.grid(True)
        plt.savefig('traffic_analysis_graph.png')
        plt.show()
        print("Graph saved as 'traffic_analysis_graph.png'")
