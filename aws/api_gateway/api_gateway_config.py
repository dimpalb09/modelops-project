# ============================================================
# aws/api_gateway/api_gateway_config.py
# Amazon API Gateway Configuration — PLACEHOLDER
#
# PURPOSE: In production, API Gateway sits in front of the
# FastAPI backend and handles routing, authentication,
# rate limiting, and HTTPS for the /predict endpoint.
#
# Pipeline Role:
#   UI → API Gateway → FastAPI (Docker/EC2) → Prediction
# ============================================================

API_GATEWAY_CONFIG = {
    # Replace with your actual API Gateway URL after deployment
    "base_url":    "https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod",
    "stage":       "prod",
    "endpoints": {
        "predict": "/predict",   # POST
        "health":  "/",          # GET
    },
    "region": "us-east-1",
    "api_name": "ModelOps-API",
}

# ---- What API Gateway does ----
# 1. Receives HTTP requests from the UI (browser)
# 2. Routes them to the FastAPI backend running in Docker
# 3. Handles HTTPS/SSL automatically (no cert setup needed)
# 4. Provides rate limiting (prevents abuse)
# 5. Can authenticate requests with API keys

# ---- HOW TO SET UP API GATEWAY ----
# 1. Go to https://console.aws.amazon.com/apigateway
# 2. Click "Create API" → "HTTP API"
# 3. Add Integration: HTTP → http://YOUR_EC2_OR_ECS_URL:8000
# 4. Add Route: POST /predict
# 5. Add Route: GET /
# 6. Deploy to stage: "prod"
# 7. Copy the Invoke URL and update the frontend script.js

# ---- UPDATING FRONTEND FOR PRODUCTION ----
# In frontend/script.js, change:
#
#   const API_URL = "http://localhost:8000/predict";
#
# To:
#   const API_URL = "https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod/predict";

print("API Gateway Config loaded (placeholder).")
print(f"Local dev URL : http://localhost:8000/predict")
print(f"Production URL: {API_GATEWAY_CONFIG['base_url']}/predict")
