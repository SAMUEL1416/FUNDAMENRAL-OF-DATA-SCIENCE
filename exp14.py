import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

data = {
    "feedback": [
        "good product",
        "excellent service",
        "good quality product",
        "service is good",
        "excellent product quality"
    ]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)


df = pd.read_csv("data.csv")


words = " ".join(df["feedback"]).lower().split()

freq = Counter(words)

top = freq.most_common(5)

print("Top Words:")
for w, c in top:
    print(w, ":", c)

x = [i[0] for i in top]
y = [i[1] for i in top]

plt.bar(x, y)
plt.title("Word Frequency")
plt.show()
