from flask import Flask, request, jsonify, render_template
import joblib  # Changed from pickle to joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load your model once when the server starts
try:
    loaded_model = joblib.load('model/hdb_resale_best_model.joblib')  # Updated path and method
    print("Model loaded successfully!")
    
    # Debug: Check what the model expects
    print(f"Model type: {type(loaded_model)}")
    if hasattr(loaded_model, 'feature_names_in_'):
        print(f"Expected features: {loaded_model.feature_names_in_}")
        
except Exception as e:
    print(f"Error loading model: {e}")
    loaded_model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if loaded_model is None:
            return jsonify({'error': 'Model not loaded'}), 500
            
        data = request.json
        print(f"Received data: {data}")  # Debug print

        if data is None:
            return jsonify({'error': 'No JSON data received'}), 400
        
        # Create DataFrame with proper column names
        df = pd.DataFrame([{
            'town': data['town'],
            'flat_type': data['flat_type'],
            'storey_range': data['storey_range'],
            'floor_area_sqm': data['floor_area_sqm'],
            'flat_model': data['flat_model'],
            'transac_year': data['transac_year'],
            'transac_month': data['transac_month'],
            'remaining_lease_by_months': data['remaining_lease_by_months']
        }])
        
        print(f"DataFrame columns: {df.columns.tolist()}")  # Debug print
        print(f"DataFrame shape: {df.shape}")  # Debug print
        print(f"DataFrame dtypes: {df.dtypes}")  # Debug print
        
        # Make prediction
        prediction = loaded_model.predict(df)[0]
        print(f"Prediction: {prediction}")  # Debug print
        
        return jsonify({'prediction': float(prediction)})
    
    except Exception as e:
        print(f"Error: {e}")  # Debug print
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)