import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("Current Folder:", os.getcwd())

csv_path = "data/calorie_dataset.csv"

print("CSV Exists:", os.path.exists(csv_path))

data = pd.read_csv(csv_path)

print(data.head())

X = data[["Age", "Gender", "Height", "Weight", "Activity"]]
y = data["Calories"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/calorie_model.pkl")

print("✅ Model Saved Successfully")