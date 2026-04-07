# ============================================================
# aws/sagemaker/sagemaker_train_script.py
# This script runs INSIDE the SageMaker instance during training.
#
# SageMaker calls this script with environment variables that
# point to where the data is and where to save the model.
# ============================================================

import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

def train():
    # ---- SageMaker passes data paths via environment variables ----
    # SM_CHANNEL_TRAIN = path to training data inside the container
    # SM_MODEL_DIR     = path where we must save the model
    train_dir = os.environ.get('SM_CHANNEL_TRAIN', '../../dataset')
    model_dir = os.environ.get('SM_MODEL_DIR',     '.')

    # ---- Load the dataset ----
    data_path = os.path.join(train_dir, 'BankChurn.csv')
    df = pd.read_csv(data_path)
    print(f"Dataset loaded: {df.shape}")

    # ---- Select features and target ----
    X = df[['Age', 'Balance', 'CreditScore']]
    y = df['Exited']

    # ---- Train/test split ----
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---- Train the model ----
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # ---- Evaluate ----
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Accuracy: {accuracy * 100:.2f}%")

    # ---- Save model — SageMaker expects it in SM_MODEL_DIR ----
    model_path = os.path.join(model_dir, 'model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to: {model_path}")

if __name__ == '__main__':
    train()
