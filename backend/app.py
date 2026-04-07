# ============================================================
# app.py
# FastAPI Backend Server
#
# LOCAL:      Accessed directly at http://localhost:8000
# PRODUCTION: Sits behind Amazon API Gateway
#             UI → API Gateway → This FastAPI app (in Docker)
# ============================================================

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import os
import datetime
import pandas as pd

# ---- AWS CloudWatch Integration (Placeholder) ----
# In production, uncomment this to log every prediction to CloudWatch
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'aws'))
# from cloudwatch.cloudwatch_monitor import log_prediction, send_metric

# ---- Step 1: Create the FastAPI app ----
app = FastAPI(
    title="ModelOps API",
    description="Bank Customer Churn Prediction — ModelOps FYP",
    version="1.0.0"
)

# ---- Step 2: CORS Middleware ----
# Required so the frontend (different port) can call this API
# In production, API Gateway also handles CORS at the gateway level
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Step 3: Load the trained model and scaler ----
# We need the scaler to transform input data before prediction
model_path  = os.path.join(os.path.dirname(__file__), 'model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("✅ model.pkl loaded successfully!")
    
    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)
    print("✅ scaler.pkl loaded successfully!")

except FileNotFoundError as e:
    print(f"❌ Error loading artifacts: {str(e)}")
    print("Run: python train_model.py first")
    model  = None
    scaler = None

# ---- Step 4: Request schema ----
class CustomerData(BaseModel):
    age: float           # e.g. 35
    balance: float       # e.g. 50000.0
    credit_score: float  # e.g. 700

# ---- Step 5: Health check endpoint ----
# GET /  →  used by Docker healthcheck and CI/CD verification
@app.get("/")
def health_check():
    return {"message": "ModelOps API Running"}

# ---- Step 6: Prediction endpoint ----
# POST /predict
# In the full architecture:
#   UI → API Gateway → POST /predict → FastAPI → model.pkl → Response
#
# CloudWatch logs each prediction for monitoring and drift detection
@app.post("/predict")
def predict(customer: CustomerData):

    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not loaded. Please run train_model.py first."
        )

    try:
        # Prepare input as a DataFrame to match the features used during training
        # Features were: ['Age', 'Balance', 'CreditScore']
        tc_df = pd.DataFrame([[customer.age, customer.balance, customer.credit_score]], 
                             columns=['Age', 'Balance', 'CreditScore'])

        # Apply the SAME scaling used during training (CRITICAL!)
        input_scaled = scaler.transform(tc_df)

        # Run prediction (returns 0 or 1)
        result = model.predict(input_scaled)[0]

        # Convert to human-readable label
        prediction_text = "Customer Will Churn" if result == 1 else "Customer Will Not Churn"

        # ---- AWS CloudWatch Logging (Placeholder) ----
        # In production, log every prediction for monitoring & drift detection
        # log_prediction(customer.age, customer.balance, customer.credit_score, prediction_text)
        # send_metric("TotalPredictions", 1)
        # if result == 1:
        #     send_metric("ChurnPredictions", 1)

        return {"prediction": prediction_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
