

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import tensorflow as tf

app = FastAPI(title="Demand Forecasting API", version="1.0")

model = tf.keras.models.load_model('demand_lstm_model.h5', compile=False)
scaler = joblib.load('scaler.pkl')

class PredictionRequest(BaseModel):
    features: list[list[float]]

@app.get("/")
def home():
    return {"message": "Demand Forecasting API is running successfully!"}

@app.post("/predict")
def predict_demand(request: PredictionRequest):
    input_data = np.array(request.features)
    
    if input_data.shape != (30, 4):
        return {"error": "Invalid input shape. Expected shape is (30, 4)"}
        
    scaled_data = scaler.transform(input_data)
    reshaped_data = np.reshape(scaled_data, (1, 30, 4))
    
    prediction = model.predict(reshaped_data)
    prediction_val = float(prediction[0][0])
    
    return {"predicted_demand": prediction_val}
