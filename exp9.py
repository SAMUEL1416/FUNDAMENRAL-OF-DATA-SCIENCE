import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 300, 250, 400, 350]

plt.figure(figsize=(10,5))


plt.subplot(1, 2, 1)
plt.plot(months, sales)
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()
