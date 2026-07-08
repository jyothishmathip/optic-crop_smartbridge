import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv("Crop_recommendation.csv")
df = df.rename(columns={"N": "nitrogen", "P": "phosphorous", "K": "potassium"})

# Outlier handling on phosphorous via IQR (same approach as project notebook)
Q1 = df["phosphorous"].quantile(0.25)
Q3 = df["phosphorous"].quantile(0.75)
IQR = Q3 - Q1
filt = (df["phosphorous"] >= Q1 - 1.5 * IQR) & (df["phosphorous"] <= Q3 + 1.5 * IQR)
df = df.loc[filt]

y = df["label"]
X = df.drop(["label"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Saved model.pkl")
