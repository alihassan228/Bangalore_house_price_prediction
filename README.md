# 🏠 Bangalore House Price Prediction App

A Machine Learning web application that predicts house prices in Bangalore based on user inputs such as location, area (sqft), number of bedrooms (BHK), and bathrooms.

This project demonstrates end-to-end ML workflow including:
- Data Cleaning
- Feature Engineering
- Model Training
- Pipeline Creation
- Model Serialization
- Flask Web App Development
- Deployment Ready Setup

---

## 🚀 Live Demo

👉 (https://huggingface.co/spaces/Alihassan228/house-prediction-model)

---

## 📌 Problem Statement

Real estate price prediction helps buyers and sellers estimate fair property values.  
This project uses historical housing data from Bangalore to train a regression model that predicts house prices.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML/CSS
- Gunicorn
- Docker (for deployment)
- Hugging Face Spaces

---

## 📊 Machine Learning Workflow

### 1️⃣ Data Preprocessing
- Handled missing values
- Removed outliers
- Cleaned inconsistent data
- Converted categorical variables using OneHotEncoder

### 2️⃣ Feature Engineering
- Extracted BHK from size column
- Converted total_sqft to numeric
- Reduced high cardinality location feature

### 3️⃣ Model Training
- Used Linear Regression
- Applied StandardScaler
- Used ColumnTransformer for encoding
- Created a full Pipeline

### 4️⃣ Model Serialization
- Saved trained model using Pickle
- Loaded model inside Flask app for prediction

---

## 📂 Project Structure

```

Bangalore_House_Price_App/
│
├── app.py
├── house_price_model.pkl
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html
├── Bengaluru_House_Data.csv
└── bengaluru_house_price_prediction.ipynb

```

---

## 💻 How to Run Locally

### 1️⃣ Clone Repository
```

git clone [https://github.com/yourusername/Bangalore-House-Price-App.git](https://github.com/yourusername/Bangalore-House-Price-App.git)
cd Bangalore-House-Price-App

```

### 2️⃣ Install Dependencies
```

pip install -r requirements.txt

```

### 3️⃣ Run Application
```

python app.py

```

Open browser and go to:

```

[http://127.0.0.1:7860/](http://127.0.0.1:7860/)

```

---

## 🌐 Deployment

This project is deployment-ready and can be deployed on:

- Hugging Face Spaces (Docker)
- Render
- Railway

---

## 📈 Model Details

- Algorithm: Linear Regression
- Pipeline: ColumnTransformer + StandardScaler + LinearRegression
- Target Variable: Price (Lakhs)
- Evaluation: R² Score

---

## 🔮 Future Improvements

- Add more advanced models (Ridge, Lasso, XGBoost)
- Add feature importance visualization
- Improve UI design
- Add model performance comparison page
- Deploy with custom domain

---

## 👨‍💻 Author

Ali Hassan  
Machine Learning Enthusiast  
Python Developer  