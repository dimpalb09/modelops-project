# ============================================================
# aws/lambda/lambda_preprocess.py
# AWS Lambda Function — PLACEHOLDER
#
# PURPOSE: This Lambda function is triggered automatically
# when a new CSV file is uploaded to the S3 bucket.
# It preprocesses the raw data and saves the cleaned version
# back to S3, ready for SageMaker training.
#
# Pipeline Role:
#   S3 Upload Event → Lambda Triggered → Clean Data → S3 Output
# ============================================================

# ---- THIS IS THE ACTUAL LAMBDA HANDLER FUNCTION ----
# In AWS Lambda, the entry point is always: lambda_handler(event, context)

import json

# import boto3        # AWS SDK — uncomment in real Lambda
# import pandas as pd # uncomment in real Lambda Layer

def lambda_handler(event, context):
    """
    This function runs automatically in AWS Lambda when a file
    is uploaded to S3.

    event: Contains info about the S3 upload (bucket, key, etc.)
    context: AWS runtime info (we don't need this)
    """

    # ---- Step 1: Get the S3 file info from the event ----
    # bucket = event['Records'][0]['s3']['bucket']['name']
    # key    = event['Records'][0]['s3']['object']['key']
    # print(f"New file uploaded: s3://{bucket}/{key}")

    # ---- Step 2: Read the CSV from S3 ----
    # s3 = boto3.client('s3')
    # obj = s3.get_object(Bucket=bucket, Key=key)
    # df = pd.read_csv(obj['Body'])

    # ---- Step 3: Preprocess the data ----
    # Keep only needed columns
    # df = df[['Age', 'Balance', 'CreditScore', 'Exited']]

    # Drop missing values
    # df = df.dropna()

    # Remove obvious outliers (CreditScore must be 300-900)
    # df = df[(df['CreditScore'] >= 300) & (df['CreditScore'] <= 900)]
    # df = df[(df['Age'] >= 18) & (df['Age'] <= 100)]
    # df = df[df['Balance'] >= 0]

    # ---- Step 4: Save cleaned data back to S3 ----
    # cleaned_key = key.replace('data/', 'data/processed_')
    # s3.put_object(
    #     Bucket=bucket,
    #     Key=cleaned_key,
    #     Body=df.to_csv(index=False)
    # )
    # print(f"Cleaned data saved to: s3://{bucket}/{cleaned_key}")

    # ---- Step 5: Return success response ----
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Preprocessing complete',
            # 'rows_processed': len(df),
            # 'output_key': cleaned_key
        })
    }


# ---- HOW TO DEPLOY THIS LAMBDA ----
# 1. Go to https://console.aws.amazon.com/lambda
# 2. Click "Create Function"
# 3. Name: modelops-preprocess
# 4. Runtime: Python 3.11
# 5. Paste this code
# 6. Add a Trigger: S3 → your bucket → "PUT" events
# 7. Add a Lambda Layer for pandas (or use AWS Data Wrangler)

# ---- LOCAL SIMULATION (runs without AWS) ----
if __name__ == "__main__":
    print("Lambda Preprocessing Placeholder")
    print("This function runs in AWS Lambda when triggered by S3 upload.")
    print("Locally, preprocessing is handled inside train_model.py")

    # Simulate the lambda call locally
    fake_event = {
        'Records': [{
            's3': {
                'bucket': {'name': 'modelops-churn-dataset'},
                'object': {'key': 'data/BankChurn.csv'}
            }
        }]
    }
    result = lambda_handler(fake_event, None)
    print(f"Lambda response: {result}")
