# ============================================================
# aws/s3/s3_config.py
# S3 Bucket Configuration — PLACEHOLDER
# ============================================================

# These are the S3 bucket settings you would use in production.
# Replace the values with your actual AWS account details.

S3_CONFIG = {
    "bucket_name":    "modelops-churn-dataset",   # Your S3 bucket name
    "region":         "us-east-1",                # AWS region
    "dataset_key":    "data/BankChurn.csv",        # S3 path for raw data
    "model_key":      "models/model.pkl",          # S3 path for trained model
    "processed_key":  "data/processed.csv",        # S3 path for cleaned data
}

# ---- HOW TO CREATE THE S3 BUCKET ----
# Option A: AWS Console
#   1. Go to https://s3.console.aws.amazon.com
#   2. Click "Create Bucket"
#   3. Enter bucket name: modelops-churn-dataset
#   4. Choose region: us-east-1
#   5. Click Create
#
# Option B: AWS CLI
#   aws s3 mb s3://modelops-churn-dataset --region us-east-1

print("S3 Config loaded (placeholder — no real AWS calls made).")
