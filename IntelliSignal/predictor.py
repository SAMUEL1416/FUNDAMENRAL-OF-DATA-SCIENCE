from collections import deque

class TrafficPredictor:
    def __init__(self, window_size=5):
        """
        Initializes the moving average predictor.
        """
        self.window_size = window_size
        self.history = deque(maxlen=window_size)

    def predict_next(self, current_count):
        """
        Calculates the moving average based on the last 'window_size' frames.
        """
        self.history.append(current_count)
        
        # Calculate moving average
        prediction = sum(self.history) / len(self.history)
        
        return round(prediction, 2)
