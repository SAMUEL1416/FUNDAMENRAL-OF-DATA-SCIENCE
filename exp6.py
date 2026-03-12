import numpy as np

time = np.array([0,1,2,3,4])
height = np.array([0,5,15,20,18])

avg_velocity = (height[-1] - height[0]) / (time[-1] - time[0])

print("Average Velocity:", avg_velocity)
