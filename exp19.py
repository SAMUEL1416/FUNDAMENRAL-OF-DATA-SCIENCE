import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Area": [800, 1000, 1200, 1500, 1800],
    "Price": [2000000, 2500000, 3000000, 3500000, 4000000]
}

df = pd.DataFrame(data)

X = df[["Area"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

new_house = pd.DataFrame({"Area":[1400]})

pred = model.predict(new_house)

print("Predicted Price:", pred[0])
