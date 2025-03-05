import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv")

# Ensure 'Profit' and 'Discount' columns exist
if "Profit" not in df.columns or "Discount" not in df.columns or "Sales" not in df.columns:
    raise ValueError("Dataset must contain 'Profit', 'Discount', and 'Sales' columns.")

# Features (Profit & Discount) and Target (Sales)
X = df[["Profit", "Discount"]]
y = df["Sales"]

# Split dataset into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
with open("sales_prediction_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model trained and saved successfully!")
