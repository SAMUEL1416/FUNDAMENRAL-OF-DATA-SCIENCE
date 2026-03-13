import pandas as pd

data = {
    "City":["Chennai","Chennai","Delhi","Delhi","Mumbai","Mumbai"],
    "Temperature":[32,34,28,30,31,33]
}

df = pd.DataFrame(data)

mean_temp = df.groupby("City")["Temperature"].mean()
print("Mean Temperature:\n",mean_temp)

std_temp = df.groupby("City")["Temperature"].std()
print("\nStandard Deviation:\n",std_temp)

range_temp = df.groupby("City")["Temperature"].max() - df.groupby("City")["Temperature"].min()

print("\nCity with highest range:", range_temp.idxmax())
print("Most consistent city:", std_temp.idxmin())
