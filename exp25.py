import pandas as pd

data = [10, 20, 20, 30, 40]

df = pd.Series(data)

print("Mean:", df.mean())
print("Median:", df.median())
print("Mode:", df.mode()[0])
