import streamlit as st
import numpy as np
import pickle
import pandas as pd
import plotly.express as px

# Set up the page layout
st.set_page_config(page_title="Supermart Sales Prediction Dashboard", layout="wide")

# Load the trained model safely
try:
    with open("sales_prediction_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error("❌ The loaded model is invalid. Please check the model file.")

# Load sales dataset
df = pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv")

# Convert 'Order Date' to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y", dayfirst=False, errors="coerce")

df = df.sort_values("Order Date")  # Sort by date

# Sidebar for inputs
st.sidebar.header("🔧 Input Features")
profit = st.sidebar.number_input("Enter Profit:", min_value=-500.0, max_value=5000.0, value=50.0)
discount = st.sidebar.slider("Select Discount:", 0.0, 1.0, 0.05)

# Prediction button
if st.sidebar.button("📊 Predict Sales"):
    if model_loaded:
        predicted_sales = model.predict(np.array([[profit, discount]]))[0]
        st.sidebar.success(f"Predicted Sales: **{predicted_sales:.2f}** 💰")
    else:
        st.sidebar.error("❌ Model not loaded. Cannot make predictions.")

# Dashboard Title
st.title("📊 Supermart Sales Analytics Dashboard")

# 1️⃣ Line Chart - Sales Trends Over Time
fig_sales_trend = px.line(df, x="Order Date", y="Sales", title="📈 Sales Trend Over Time", markers=True)
st.plotly_chart(fig_sales_trend, use_container_width=True)

# 2️⃣ Bar Chart - Sales by Category
fig_category = px.bar(df, x="Category", y="Sales", title="📊 Sales by Category", color="Category")
st.plotly_chart(fig_category, use_container_width=True)

# 3️⃣ Scatter Plot - Profit vs Discount
fig_scatter = px.scatter(df, x="Discount", y="Profit", title="📉 Profit vs. Discount", color="Category", size="Sales")
st.plotly_chart(fig_scatter, use_container_width=True)

# 4️⃣ Sales Summary
st.header("📌 Sales Summary")
st.write(df.describe())
