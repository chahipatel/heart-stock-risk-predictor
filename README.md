# ❤️ Heart Stock Risk Predictor

## 📘 Project Description

Heart Stock Risk Predictor is a Machine Learning powered healthcare application designed to predict the likelihood of heart disease based on patient health parameters. The project utilizes an XGBoost Classifier trained on a Kaggle and provides real time predictions through an interactive Streamlit web application.

The objective of this project is to demonstrate a complete end to end Machine Learning workflow, including data collection, preprocessing, exploratory data analysis, model selection, hyperparameter tuning, evaluation, and deployment. Users can enter patient information such as age, cholesterol level, blood pressure, chest pain type, and other clinical indicators to instantly assess potential heart disease risk.

This project showcases how Artificial Intelligence and Machine Learning can assist in healthcare analytics and support early risk assessment.

---

# ✨ Features

* ⚡ Real Time Prediction Results
* 🤖 XGBoost Based Classification Model
* 📊 Interactive Streamlit Web Interface
* 📝 User Friendly Input Form
* 🔄 Automated Data Preprocessing
* 📈 Machine Learning Model Optimization
* 💾 Model Persistence Using Joblib
* ☁️ Cloud Deployment with Streamlit Community Cloud
* 📱 Responsive and Easy to Use Interface

---

# 💻 Tech Stack

## Programming Language

* Python

## Data Analysis & Visualization

* Pandas
* NumPy
* Matplotlib
* Seaborn

## Machine Learning

* Scikit Learn
* XGBoost

## Model Selection & Optimization

* Train Test Split
* Cross Validation
* GridSearchCV

## Data Preprocessing

* StandardScaler
* One Hot Encoding
* Feature Engineering

## Model Persistence

* Joblib

## Web Application

* Streamlit

## Deployment

* GitHub
* Streamlit Community Cloud

---

# 📂 Dataset

### Dataset Source

Kaggle Heart Disease Dataset

The dataset contains important clinical and medical attributes used to predict cardiovascular disease risk, including:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise Induced Angina
* Oldpeak
* ST Slope

The dataset was cleaned, analyzed, transformed, and prepared before model training.

---

# 🧠 Machine Learning Pipeline

## 1. Data Collection

* Heart Disease Dataset obtained from Kaggle.

## 2. Data Understanding

* Understanding dataset structure
* Identifying feature types
* Understanding target variable

## 3. Data Cleaning

* Checking missing values
* Removing inconsistencies
* Validating feature quality

## 4. Exploratory Data Analysis (EDA)

* Correlation Analysis
* Feature Distribution Analysis
* Risk Pattern Identification
* Outlier Detection
* Statistical Analysis

### Visualization Tools Used

* Matplotlib
* Seaborn

## 5. Feature Engineering

* One Hot Encoding
* Feature Transformation
* Feature Selection

## 6. Data Scaling

* StandardScaler applied to numerical features

## 7. Data Splitting

* Training Dataset
* Testing Dataset

## 8. Model Selection

Multiple Machine Learning models were tested and compared:

* Logistic Regression
* K Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* XGBoost Classifier

## 9. Hyperparameter Tuning

* GridSearchCV used for optimization
* Parameter combinations tested
* Best performing configuration selected

## 10. Model Evaluation

Evaluation metrics used:

* Accuracy Score
* Confusion Matrix
* Classification Report
* Cross Validation

## 11. Final Model Selection

After comparison and tuning, XGBoost achieved the highest performance and was selected as the final model.

## 12. Model Serialization

The trained model and preprocessing objects were saved using Joblib:

* XGB.pkl
* scaler.pkl
* columns.pkl

## 13. Deployment

* Streamlit Application Development
* GitHub Repository Hosting
* Streamlit Community Cloud Deployment

---

# 📊 Model Performance

| Metric     | Value                        |
| ---------- | ---------------------------- |
| Model      | XGBoost Classifier           |
| Accuracy   | 88%                          |
| Dataset    | Kaggle Heart Disease Dataset |
| Deployment | Streamlit Cloud              |

### Performance Summary

The XGBoost Classifier achieved approximately **89% accuracy** on unseen test data, making it a reliable model for educational and analytical healthcare applications.

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/heart-stock-risk-predictor.git
cd heart-stock-risk-predictor
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

---

# 🧪 Usage

### Step 1

Open the application in your browser.

### Step 2

Enter patient medical information:

* Age
* Sex
* Chest Pain Type
* Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* ECG Results
* Heart Rate
* Exercise Angina
* Oldpeak
* ST Slope

### Step 3

Click the **Predict Risk** button.

### Step 4

View the prediction result:

* ✅ Low Risk of Heart Disease

or

* ⚠️ High Risk of Heart Disease

---

# 🌐 Live Demo

### Deployed Application

https://heart-stock-risk-predictor-rzsmhyf4zjwwm65s7a7y4x.streamlit.app/

---

# 📁 Project Structure

```text
heart-stock-risk-predictor/
│
├── app.py
├── XGB.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
├── README.md
```

---

# 🔮 Future Improvements

* 📊 Prediction Probability Score
* 📈 Interactive Health Dashboard
* 📝 Downloadable Prediction Reports
* 🤖 AI-Powered Health Assistant
* 📉 Advanced Risk Visualization
* 🏥 Doctor Recommendation System
* ☁️ Database Integration
* 📱 Mobile Application Version
* 🔍 Explainable AI (XAI) Integration
* 📊 Feature Importance Visualization

---

# ✨ Closing Note

Heart Stock Risk Predictor demonstrates the practical application of Machine Learning in healthcare analytics. By combining data preprocessing, exploratory data analysis, feature engineering, model optimization, evaluation, and deployment, this project showcases a complete end-to-end Machine Learning workflow.

This project reflects how Artificial Intelligence can assist in early disease risk assessment and support data-driven healthcare decision-making. It also highlights the importance of responsible AI usage in healthcare-related applications.

