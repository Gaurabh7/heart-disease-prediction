# ❤️ Heart Disease Prediction using Machine Learning

## 📋 Project Overview

This project is a machine learning-based web application for predicting the likelihood of heart disease using clinical and physiological patient information.

The system uses a **Random Forest Classifier** trained on the Heart Disease dataset. A Streamlit web interface allows users to enter patient information and receive a prediction along with the estimated prediction probability.

## 🌐 Live Demo

**[Open the Heart Disease Prediction App](https://heart-disease-prediction--git.streamlit.app/)**

https://heart-disease-prediction--git.streamlit.app/

## 🎯 Features

- ❤️ Heart disease prediction using Machine Learning
- 🌐 Interactive Streamlit web application
- 👤 Patient information input form
- 📊 Prediction probability
- 📋 Patient input summary
- 🌲 Random Forest classification model
- 🚀 Web-based deployment

## 📊 Dataset

The project uses the **Heart Disease dataset**, containing clinical and physiological attributes such as:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope

The target variable represents the presence or absence of heart disease.

## 🤖 Machine Learning Model

The project uses a **Random Forest Classifier** for prediction.

### Model Configuration

- Algorithm: Random Forest Classifier
- Number of estimators: 200
- Train-test split: 80:20
- Random state: 42
- Evaluation metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score

The trained model achieved approximately **92.86% test accuracy** on the dataset split used for this project.

> This accuracy represents performance on the project's test dataset and should not be interpreted as medical diagnostic accuracy.

## ⚙️ Methodology

### 1. Data Preparation

- Load the Heart Disease dataset
- Separate features and target variable
- Split the dataset into training and testing sets

### 2. Model Training

A Random Forest classification model is trained using the training dataset.

### 3. Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Classification Report

### 4. Prediction

The trained model is saved as a `.pkl` file and integrated into the Streamlit application.

## 🖥️ Web Application

The application is developed using **Streamlit**.

Users can enter:

- Age
- Sex
- Chest pain type
- Resting blood pressure
- Cholesterol
- Fasting blood sugar
- Resting ECG
- Maximum heart rate
- Exercise-induced angina
- Oldpeak
- ST slope

After submitting the information, the application provides a heart disease prediction and prediction probability.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

## 📁 Project Structure

```text
heart-disease-prediction/
│
├── app.py
├── random_forest_model.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   └── heart_statlog_cleveland_hungary_final.csv
│
├── script/
│   ├── train_model.py
│   ├── 10892938 - Project_Code.py
│   └── 10892938 - Project_Code.ipynb
│
└── doc/
    └── 10892938 - PROJ 518 FINAL DISSERTATION.pdf
