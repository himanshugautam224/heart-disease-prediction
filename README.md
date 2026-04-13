"""
# ❤️ Heart Disease Prediction System

This project is a Machine Learning-based web application built using Streamlit that predicts the likelihood of heart disease.

## 🚀 Features
- User-friendly UI
- Real-time prediction
- Based on trained ML model

## 📂 Files Required
- app.py
- model.pkl (exported from your Jupyter Notebook)
-heart_data.csv

## 🛠️ How to Export Model from .ipynb

```python
import joblib
joblib.dump(model, "model.pkl")
```

## ▶️ Run the App

```bash
pip install streamlit joblib numpy
streamlit run app.py
```

## 📊 Input Parameters
- Age
- Sex
- Chest Pain Type
- Blood Pressure
- Cholesterol
- And more...

## 🧠 Model
Trained using classification algorithms like Logistic Regression / Random Forest .

## 👨‍💻 Author
Himanshu Gautam

"""
