# ============================================================
# aws/sagemaker/sagemaker_train.py
# Amazon SageMaker Training Job — PLACEHOLDER
#
# PURPOSE: In production, this script submits a training job
# to Amazon SageMaker, which trains the model on cloud GPUs/CPUs
# and saves the trained model artifact back to S3.
#
# Pipeline Role:
#   S3 (clean data) → SageMaker Training Job → model.pkl → S3
# ============================================================

# import boto3
# import sagemaker
# from sagemaker.sklearn.estimator import SKLearn

# ---- SageMaker Configuration ----
SAGEMAKER_CONFIG = {
    "role":            "arn:aws:iam::YOUR_ACCOUNT_ID:role/SageMakerRole",
    "instance_type":   "ml.m5.large",     # Cheapest instance for small datasets
    "instance_count":  1,
    "framework_version": "1.2-1",         # scikit-learn version
    "input_s3":        "s3://modelops-churn-dataset/data/processed.csv",
    "output_s3":       "s3://modelops-churn-dataset/models/",
    "job_name":        "modelops-churn-training",
}

def train_on_sagemaker():
    """
    Submits a training job to Amazon SageMaker.
    SageMaker will spin up a cloud instance, run the training
    script, and save the model to S3 automatically.
    """

    # ---- Step 1: Connect to SageMaker ----
    # session = sagemaker.Session()
    # print(f"SageMaker session started in region: {session.boto_region_name}")

    # ---- Step 2: Define the Estimator ----
    # An Estimator tells SageMaker WHAT to train and HOW
    # sklearn_estimator = SKLearn(
    #     entry_point='sagemaker_train_script.py',  # Our training code
    #     role=SAGEMAKER_CONFIG['role'],
    #     instance_type=SAGEMAKER_CONFIG['instance_type'],
    #     instance_count=SAGEMAKER_CONFIG['instance_count'],
    #     framework_version=SAGEMAKER_CONFIG['framework_version'],
    #     output_path=SAGEMAKER_CONFIG['output_s3'],
    # )

    # ---- Step 3: Start the Training Job ----
    # sklearn_estimator.fit({'train': SAGEMAKER_CONFIG['input_s3']})
    # print("SageMaker training complete!")
    # print(f"Model saved to: {SAGEMAKER_CONFIG['output_s3']}")

    pass


# ---- HOW TO SET UP SAGEMAKER ----
# 1. Go to https://console.aws.amazon.com/sagemaker
# 2. Create an IAM Role with SageMaker permissions
# 3. Update SAGEMAKER_CONFIG['role'] above with your ARN
# 4. Install: pip install sagemaker boto3
# 5. Run: python sagemaker_train.py

# ---- LOCAL EQUIVALENT ----
# Locally, we use train_model.py which does the same thing
# but runs on your own machine instead of AWS cloud.

if __name__ == "__main__":
    print("SageMaker Training Placeholder")
    print("This would submit a cloud training job to Amazon SageMaker.")
    print("Locally, use: python backend/train_model.py")
    print(f"\nConfig: {SAGEMAKER_CONFIG}")
