from flask import Flask, request, render_template
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load the model, scaler, and encoder
model = joblib.load('models/best_model.pkl')
scaler = joblib.load('models/scaler.pkl')
encoder = joblib.load('models/ordinal_encoder.pkl')


# Home route
@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        new_data = {
            'GRE Score': float(request.form['gre_score']),
            'TOEFL Score': float(request.form['toefl_score']),
            'University Rating': int(request.form['university_rating']),
            'SOP': float(request.form['sop']),
            'LOR': float(request.form['lor']),
            'CGPA': float(request.form['cgpa']),
            'Research': int(request.form['research'])
        }

        # Create DataFrame
        input_df = pd.DataFrame([new_data])
        
        # Scale the new input data
        input_df[['GRE Score', 'TOEFL Score', 'CGPA']] = scaler.transform(input_df[['GRE Score', 'TOEFL Score', 'CGPA']])
        
        # Encode the ordinal features
        input_df[['University Rating', 'SOP', 'LOR']] = encoder.transform(input_df[['University Rating', 'SOP', 'LOR']])
        
        # Predict with the loaded model
        new_prediction = model.predict(input_df)
        new_prediction = np.clip(new_prediction, 0, 1)  # Clip prediction to ensure it's within the range [0, 1]
        
        prediction_text = f'Admission Probability: {round(float(new_prediction * 100), 2)}%'
        return render_template('index.html', prediction_text=prediction_text)
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
