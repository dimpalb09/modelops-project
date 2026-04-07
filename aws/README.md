# AWS Integration Guide — ModelOps Project

This folder contains **placeholder files** for all AWS services used in the ModelOps architecture.
All files are fully commented and ready to activate with real AWS credentials.

## Services Overview

| Service           | File                                      | Purpose                              |
|-------------------|-------------------------------------------|--------------------------------------|
| Amazon S3         | `s3/upload_dataset.py`                    | Store raw dataset + model artifacts  |
| Amazon S3         | `s3/s3_config.py`                         | Bucket configuration                 |
| AWS Lambda        | `lambda/lambda_preprocess.py`             | Auto-preprocess data on S3 upload    |
| Amazon SageMaker  | `sagemaker/sagemaker_train.py`            | Submit cloud training job            |
| Amazon SageMaker  | `sagemaker/sagemaker_train_script.py`     | Training code that runs in cloud     |
| Amazon CloudWatch | `cloudwatch/cloudwatch_monitor.py`        | Log predictions + detect drift       |
| API Gateway       | `api_gateway/api_gateway_config.py`       | Route UI requests to backend         |

## Full AWS Pipeline Flow

```
GitHub Push
    ↓
GitHub Actions (CI/CD)
    ↓
Train Model → Docker Build → Docker Image Updated
    ↓
Amazon S3 (dataset stored)
    ↓
AWS Lambda (preprocess data)
    ↓
Amazon SageMaker (train model in cloud)
    ↓
API Gateway Endpoint
    ↓
Docker Container (FastAPI)
    ↓
Amazon CloudWatch (monitor logs + detect drift)
    ↓ (if drift detected)
Trigger Retraining (SNS Alert → SageMaker)
```

## To Activate AWS Integration

1. Create an AWS account at https://aws.amazon.com
2. Install AWS CLI: `pip install awscli`
3. Configure credentials: `aws configure`
4. Uncomment the code in each placeholder file
5. Follow the setup instructions inside each file

## For the Viva / Demo

You can explain each AWS service's role:

- **S3** = "Cloud storage for our dataset. Like Google Drive but for code."
- **Lambda** = "Serverless function that auto-cleans data when new files are uploaded."  
- **SageMaker** = "Managed ML training service. We just send data, it trains and returns the model."
- **CloudWatch** = "Dashboard that monitors API performance and alerts if model accuracy drops."
- **API Gateway** = "The front door to our backend. Handles HTTPS and routing securely."
- **GitHub Actions** = "Every time we push code, it automatically trains and deploys the model."
