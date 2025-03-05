import pickle
import pandas as pd

# Load the trained model
with open("sales_prediction_model.pkl", "rb") as file:
    model = pickle.load(file)

# Prepare input as a DataFrame with feature names
input_data = pd.DataFrame([[50, 0.2]], columns=["Profit", "Discount"])
predicted_sales = model.predict(input_data)[0]

print(f"📊 Predicted Sales: {predicted_sales:.2f}")

