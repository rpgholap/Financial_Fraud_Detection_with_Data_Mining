# Financial Fraud Detection System

This project implements a **Financial Fraud Detection System** that uses machine learning to predict fraudulent transactions based on transaction details. A **Decision Tree Classifier** is trained on the data and deployed using a **Flask web application** for user interaction.

## Project Overview

The system predicts whether a transaction is fraudulent or not based on various features like transaction type, amount, and account balances. It uses a trained machine learning model and exposes this functionality through a Flask-based web interface.

## Features

- **Data Preprocessing**: Handles missing values and encodes categorical variables.
- **Model Training**: A decision tree classifier is used to predict if a transaction is fraudulent or not.
- **Web Interface**: Allows users to input transaction details and get predictions via a simple form.
- **Error Handling**: In case of invalid inputs, the system returns appropriate error messages.

## Example Use Case

- Example 1: Non-Fraudulent Transaction
  Input:

  Type: PAYMENT
  Amount: 1000.00
  Old Balance: 5000.00
  New Balance: 4000.00
  Output:

  Prediction: No Fraud
  In this example, the transaction is considered non-fraudulent based on the amount and balance changes. A payment of 1000.00 from an account with 5000.00 balance, leaving a remaining balance of 4000.00, is 
  typical behavior.

- Example 2: Fraudulent Transaction
  Input:

  Type: TRANSFER
  Amount: 20000.00
  Old Balance: 10000.00
  New Balance: 0.00
  Output:
  
  Prediction: Fraud
  In this case, the system detects a potentially fraudulent transaction due to the large transfer amount of 20000.00, which exceeds the account balance of 10000.00, leading to a balance of 0.00. This scenario is 
  considered suspicious and flagged as fraud.

## Requirements

- Python 3.x
- Flask
- Pandas
- Numpy
- scikit-learn
- joblib


