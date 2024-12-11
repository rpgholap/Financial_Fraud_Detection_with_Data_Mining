from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load your dataset
df = pd.read_csv(r"C:/DataSet/online_fraud_detection.csv")

# Preprocess the dataset
df = df.dropna()  # Remove rows with any missing values
df['isFraud'] = df['isFraud'].map({0: 'No Fraud', 1: 'Fraud'})
df['type'] = df['type'].map({'PAYMENT': 1, 'TRANSFER': 4, 'CASH_OUT': 2, 'DEBIT': 5, 'CASH_IN': 3})

# Define features and target variable
x = df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig']]
y = df['isFraud']

# Split data into training and testing sets
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.20, random_state=42)

# Train your model
model = DecisionTreeClassifier()
model.fit(xtrain, ytrain)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        type_val = int(request.form['type'])
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])

        # Make a prediction using the loaded model
        input_data = np.array([type_val, amount, oldbalanceOrg, newbalanceOrig]).reshape(1, -1)
        prediction = model.predict(input_data)

        # Return prediction result to the result.html template
        result = 'Fraud' if prediction[0] == 'Fraud' else 'No Fraud'
        return render_template('result1.html', result=result)

    except Exception as e:
        return render_template('error1.html', error=e)

if __name__ == '__main__':
    app.run(debug=True)
