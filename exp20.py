import pandas as pd

data = {
    "Study_Hours": [2,3,4,5,6],
    "Marks": [50,55,65,70,80]
}

df = pd.DataFrame(data)

correlation = df.corr()

print("Correlation Matrix:\n", correlation)
