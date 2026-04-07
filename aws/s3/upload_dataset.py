# ============================================================
# aws/s3/upload_dataset.py
# AWS PLACEHOLDER FILE — NOT REQUIRED TO RUN LOCALLY
#
# PURPOSE: In production, this script uploads the raw dataset
# to Amazon S3 so it can be accessed by Lambda and SageMaker.
#
# Pipeline Role:
#   LOCAL CSV → Amazon S3 Bucket → AWS Lambda (preprocessing)
# ============================================================

# ---- TO USE THIS IN PRODUCTION ----
# pip install boto3
# Set your AWS credentials via:
#   aws configure   (or set env variables)

# import boto3
# import os

# S3_BUCKET_NAME = "modelops-churn-dataset"   # Your S3 bucket name
# S3_KEY         = "data/BankChurn.csv"        # Path inside the bucket
# LOCAL_FILE     = "../../dataset/BankChurn.csv"

# def upload_dataset():
#     s3 = boto3.client('s3')
#     print(f"Uploading {LOCAL_FILE} to s3://{S3_BUCKET_NAME}/{S3_KEY} ...")
#     s3.upload_file(LOCAL_FILE, S3_BUCKET_NAME, S3_KEY)
#     print("Upload complete!")

# if __name__ == "__main__":
#     upload_dataset()

# ---- WHAT THIS DOES IN THE FULL PIPELINE ----
# 1. The raw BankChurn.csv is stored in S3 (acts as a data lake)
# 2. Any new data can be dropped into S3 to trigger retraining
# 3. SageMaker reads the dataset directly from this S3 path
# 4. Model artifacts (.pkl) are also saved back to S3 after training

print("AWS S3 Placeholder — Uncomment code above to use with real AWS credentials.")
print("Locally, the dataset is read from: dataset/BankChurn.csv")
