from flask import Flask, render_template, request
import pandas as pd
import joblib
import os
from tensorflow.keras.models import load_model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/technology')
def technology():
    return render_template('technology.html')

@app.route('/team')
def team():
    return render_template('team.html')

# Load models and preprocessors
model1 = model2 = preprocessor1 = preprocessor2 = None

try:
    model1 = load_model('fraud_dcn_model_forced_under97.h5')
    print("Model1 loaded successfully.")
except Exception as e:
    print("Error loading model1:", e)

try:
    model2 = load_model('fraud_modelx.h5')
    print("Model2 loaded successfully.")
except Exception as e:
    print("Error loading model2:", e)

try:
    preprocessor1 = joblib.load('preprocessor_dcn.pkl')
    print("Preprocessor1 loaded successfully.")
except Exception as e:
    print("Error loading preprocessor1:", e)

try:
    preprocessor2 = joblib.load('preprocessor.pkl')
    print("Preprocessor2 loaded successfully.")
except Exception as e:
    print("Error loading preprocessor2:", e)

# Risk level logic
def get_risk_level(score):
    if score >= 0.85:
        return 'High Risk'
    elif score >= 0.5:
        return 'Medium Risk'
    elif score >= 0.2:
        return 'Low Risk'
    else:
        return 'Very Low Risk'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {
            'Hour_of_Day': int(request.form['Hour_of_Day']),
            'Amount': float(request.form['Amount']),
            'V1': float(request.form['V1']),
            'V2': float(request.form['V2']),
            'V3': float(request.form['V3']),
            'V4': float(request.form['V4']),
            'V5': float(request.form['V5']),
            'Merchant_Type': request.form['Merchant_Type'],
            'Location_Distance': float(request.form['Location_Distance']),
            'Transaction_Frequency': float(request.form['Transaction_Frequency']),
            'Is_International': int(request.form['Is_International']),
            'Device_Type': request.form['Device_Type']
        }

        def model_predict(model, preprocessor):
            df = pd.DataFrame([data])
            X_processed = preprocessor.transform(df)
            pred = model.predict(X_processed)[0][0]
            return pred

        result1 = result2 = None
        risk_flag1 = risk_flag2 = None  # True if fraud, False if not fraud
        score1 = score2 = None

        if model1 and preprocessor1:
            score1 = model_predict(model1, preprocessor1)
            risk_flag1 = score1 >= 0.5
            result1 = {
                "score": f"{round(score1 * 100, 2)}%",
                "result": "Fraud" if risk_flag1 else "Not Fraud",
                "risk_level": get_risk_level(score1)
            }

        if model2 and preprocessor2:
            score2 = model_predict(model2, preprocessor2)
            risk_flag2 = score2 >= 0.5
            result2 = {
                "score": f"{round(score2 * 100, 2)}%",
                "result": "Fraud" if risk_flag2 else "Not Fraud",
                "risk_level": get_risk_level(score2)
            }

        # Combine total risk based on both models' risk flags
        if risk_flag1 is None and risk_flag2 is None:
            total_risk = None  # no models available
        elif risk_flag1 is not None and risk_flag2 is not None:
            if risk_flag1 and risk_flag2:
                total_risk = "Risk"
            elif not risk_flag1 and not risk_flag2:
                total_risk = "Not Risk"
            else:
                total_risk = "Moderate Risk"
        else:
            # Only one model available
            total_risk = "Risk" if (risk_flag1 or risk_flag2) else "Not Risk"

        # Calculate average score if both scores exist
        if score1 is not None and score2 is not None:
            avg_score = round(((score1 + score2) / 2) * 100, 2)
        elif score1 is not None:
            avg_score = round(score1 * 100, 2)
        elif score2 is not None:
            avg_score = round(score2 * 100, 2)
        else:
            avg_score = None

        return render_template(
            'result.html',
            result1=result1,
            result2=result2,
            total_risk=total_risk,
            avg_score=avg_score
        )

    except Exception as e:
        return f"Error occurred during prediction: {e}"

if __name__ == '__main__':
    app.run(debug=True)
