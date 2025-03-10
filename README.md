
# 🛒 Sales Analysis Dashboard

## 📌 Overview
This project analyzes **Supermart Grocery Sales Data** to extract key business insights and trends. It includes **Exploratory Data Analysis (EDA), sales forecasting, and customer insights**, all presented through an **interactive Streamlit dashboard**.

## 🚀 Features
- ✅ **Sales Distribution Analysis** – Identify peak sales months & seasonal trends.  
- ✅ **Regional & Category-wise Sales** – Find top-performing locations and product categories.  
- ✅ **Customer Behavior Insights** – Analyze repeat purchases and buying patterns.  
- ✅ **Sales Forecasting** – Predict future sales using machine learning models.  
- ✅ **Streamlit Dashboard** – Interactive visualization for real-time exploration.  

## 🛠️ Tech Stack
- **Python** – Pandas, NumPy (Data Processing)  
- **Matplotlib & Seaborn** – Data Visualization  
- **Scikit-learn** – Forecasting & Predictive Analytics  
- **Streamlit** – Web-based Interactive Dashboard  

## 📊 Dashboard Preview
![Screenshot (64)](https://github.com/user-attachments/assets/d47a388a-e8d8-4988-8bd5-d7f45ac4357f)
![Screenshot (58)](https://github.com/user-attachments/assets/3aa891e4-3dbd-486a-a987-aed2a0b75b12)
![Screenshot (59)](https://github.com/user-attachments/assets/08098e5d-f5f0-4b59-9ee5-554ae7ab4bae)
![Screenshot (60)](https://github.com/user-attachments/assets/a92a8ecd-ec05-4979-81b6-9937ecc0d53e)
![Screenshot (61)](https://github.com/user-attachments/assets/235325b5-1ee9-472e-929b-c292c26cbbff)

## 📂 Dataset
The dataset used in this project is **Supermart Grocery Sales - Retail Analytics Dataset** containing:  
- **Date** (Transaction date)  
- **Product Categories**  
- **Sales Amount**  
- **Customer Segments & Regions**  

## 🔧 Installation & Usage
### 1️⃣ Clone the repository:  
```bash
git clone https://github.com/yourusername/sales-analysis-dashboard.git
cd sales-analysis-dashboard
```
### 2️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Streamlit dashboard:  
```bash
streamlit run dashboard.py
```

## 🔍 Common Issues & Fixes
### ⚠️ Streamlit "Missing ScriptRunContext" Warning
**Issue:** When running `python dashboard.py`, Streamlit throws a **missing ScriptRunContext** warning.  
**Fix:** Run the command with Streamlit instead:
```bash
streamlit run dashboard.py
```

### ⚠️ DataFrame Arrow Serialization Error
**Issue:** PyArrow fails to convert `Order Date` due to incorrect formatting.  
**Fix:** Ensure the column is in the correct datetime format before passing it to Streamlit:
```python
import pandas as pd

# Load dataset
df = pd.read_csv("your_dataset.csv")

# Convert 'Order Date' column to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

# Drop any rows with NaT values
df = df.dropna(subset=["Order Date"])
```

## 📈 Insights & Findings
- 📊 **September had the highest sales volume**, indicating seasonal demand.  
- 🛍️ **Electronics & Grocery categories dominated total sales.**  
- 🔄 **Repeat customers contributed significantly to revenue growth.**  
- 📈 **Forecasting models predict a steady increase in sales for the next quarter.**  

## 🤝 Contributing
Feel free to fork this repo, raise issues, or submit pull requests to improve functionality! 🚀  

## 🏆 Acknowledgments
Special thanks to **Supermart Grocery Sales Dataset** and the open-source community.  

---

🔹 **Author:** Niyati Thacker 
🔹 **LinkedIn:**  www.linkedin.com/in/niyati-thacker


