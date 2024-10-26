from flask import Flask, request, render_template
from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load the model, LOR mean, scaler, and encoder for prediction
loaded_data = joblib.load('models/final_model_with_lor_mean.pkl')
model = loaded_data["model"]
lor_mean = loaded_data["lor_mean"]
lor_mean = np.floor(lor_mean)  # Optional: rounding to nearest integer

with open('models/scaler.pkl', 'rb') as file:
    scaler = joblib.load(file)
with open('models/ordinal_encoder.pkl', 'rb') as file:
    encoder = joblib.load(file)

# Home route
@app.route('/')
def home():
    return render_template('index.html', prediction_text='', lor_mean=lor_mean)

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form, using lor_mean if LOR is left blank
        lor_value = request.form['lor']
        lor_value = lor_mean if lor_value == '' else float(lor_value)
        
        new_data = {
            'GRE Score': float(request.form['gre_score']),
            'TOEFL Score': float(request.form['toefl_score']),
            'LOR': lor_value,
            'CGPA': float(request.form['cgpa']),
            'Research': int(request.form['research'])
        }

        # Create DataFrame
        input_df = pd.DataFrame([new_data])
        
        # Scale the new input data
        input_df[['GRE Score', 'TOEFL Score', 'CGPA']] = scaler.transform(input_df[['GRE Score', 'TOEFL Score', 'CGPA']])
        
        # Encode the ordinal features
        input_df['LOR'] = encoder.transform(input_df[['LOR']])
        
        # Predict with the loaded model
        new_prediction = model.predict(input_df)
        new_prediction = np.clip(new_prediction, 0, 1)  # Clip prediction to ensure it's within the range [0, 1]
        
        prediction_text = f'Admission Probability: {round(float(new_prediction * 100), 2)}%'
        
        return render_template('index.html', prediction_text=prediction_text, lor_mean=lor_mean)
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}', lor_mean=lor_mean)

if __name__ == "__main__":
    app.run(debug=True)
