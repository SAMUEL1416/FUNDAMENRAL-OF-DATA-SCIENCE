import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
temperature = [25, 28, 30, 35, 33]
rainfall = [10, 20, 5, 15, 8]

# Line Plot for Temperature
plt.plot(months, temperature)
plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.show()

# Scatter Plot for Rainfall
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.show()
