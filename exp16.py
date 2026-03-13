import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


data = {
    "age":[25,35,45,50,23,40],
    "bp":[120,130,140,135,118,145],
    "cholesterol":[200,210,190,220,180,230],
    "outcome":["Good","Bad","Good","Bad","Good","Bad"]
}

df = pd.DataFrame(data)


df["outcome"] = df["outcome"].map({"Good":1,"Bad":0})

X = df[["age","bp","cholesterol"]]
y = df["outcome"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test,pred))
print("\nClassification Report:\n",classification_report(y_test,pred))
