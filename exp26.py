import numpy as np

data = np.array([10, 20, 30, 40, 50])

normalized = (data - data.min()) / (data.max() - data.min())

print("Normalized Data:", normalized)
