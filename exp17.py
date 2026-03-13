import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    "Customer_ID":[1,2,3,4,5,6],
    "Amount_Spent":[200,500,150,800,120,700],
    "Visits":[5,10,3,15,2,12]
}

df = pd.DataFrame(data)

X = df[["Amount_Spent","Visits"]]

kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(X)

print(df)

# Visualization
plt.scatter(df["Amount_Spent"], df["Visits"], c=df["Cluster"])
plt.title("Customer Segments")
plt.xlabel("Amount Spent")
plt.ylabel("Visits")
plt.show()
