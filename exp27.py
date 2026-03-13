import pandas as pd
import numpy as np

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [80, np.nan, 70, np.nan]
}

df = pd.DataFrame(data)

# Fill missing values with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df)
