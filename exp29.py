import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, 45, 75, 60]
}

df = pd.DataFrame(data)

sorted_data = df.sort_values(by="Marks", ascending=False)

print(sorted_data)
