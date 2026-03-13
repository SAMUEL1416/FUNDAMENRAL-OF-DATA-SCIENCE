import pandas as pd

data = {
    "Name": ["A","B","C","D"],
    "Marks": [80,45,60,30]
}

df = pd.DataFrame(data)

# Students with marks > 50
filtered = df[df["Marks"] > 50]

print(filtered)
