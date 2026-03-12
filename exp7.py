import numpy as np
import pandas as pd

house_data = np.array([
    [3, 1200, 5000000],
    [5, 2000, 9000000],
    [4, 1500, 6500000],
    [6, 2500, 12000000],
    [2, 1000, 4000000]
])

df = pd.DataFrame(house_data,columns=["Bedrooms", "Square_Feet", "Sale_Price"])

filtered_df = df[df["Bedrooms"] > 4]

avg_price = np.mean(filtered_df["Sale_Price"])

print("Filtered Houses (>4 Bedrooms):\n")
print(filtered_df)

print("\nAverage Sale Price (>4 Bedrooms):", avg_price)
