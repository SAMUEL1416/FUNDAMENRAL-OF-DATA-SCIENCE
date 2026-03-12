import numpy as np

fuel_efficiency = np.array([20, 25, 30, 35, 28])

average_efficiency = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency)

model1 = fuel_efficiency[0]
model2 = fuel_efficiency[1]

percentage_improvement = ((model2 - model1) / model1) * 100
print("Percentage Improvement from Model1 to Model2:", percentage_improvement, "%")
