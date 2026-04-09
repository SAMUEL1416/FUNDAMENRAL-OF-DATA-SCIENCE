class TrafficAnalyzer:
    def __init__(self, frame_width):
        """
        Initializes the lane-wise analyzer. 
        Divides the frame width into 3 vertical lanes.
        """
        self.frame_width = frame_width
        self.lane_width = frame_width // 3
        
        # Ranges for signal timings based on traffic density
        self.density_config = {
            'LOW': (0, 10, 20),      # (min, max, signal_time)
            'MEDIUM': (11, 20, 40),
            'HIGH': (21, 100, 60)
        }

    def analyze_lanes(self, detections):
        """
        Counts vehicles in each of the 3 lanes.
        """
        lane_counts = [0, 0, 0]
        
        for d in detections:
            x1, y1, x2, y2 = d['bbox']
            # Calculate the horizontal center of the vehicle
            center_x = (x1 + x2) // 2
            
            if center_x < self.lane_width:
                lane_counts[0] += 1
            elif center_x < 2 * self.lane_width:
                lane_counts[1] += 1
            else:
                lane_counts[2] += 1
                
        return lane_counts

    def get_density_info(self, lane_counts, is_emergency=False):
        """
        Classifies traffic density and identifies the lane that needs priority.
        """
        # Find which lane has the most vehicles
        max_vehicles = max(lane_counts)
        priority_lane_idx = lane_counts.index(max_vehicles)
        priority_lane_name = f"Lane {priority_lane_idx + 1}"

        if is_emergency:
            # Emergency override (usually for the lane where it was detected, 
            # but for this simulation, we prioritize all)
            return "EMERGENCY", 90, "ALL LANES (CLEARANCE)"
        
        if max_vehicles <= 5:
            return "LOW", 20, priority_lane_name
        elif 6 <= max_vehicles <= 10:
            return "MEDIUM", 40, priority_lane_name
        else:
            return "HIGH", 60, priority_lane_name
