# ============================================================
# train_model.py
# This script loads the Bank Churn dataset, trains a simple
# Logistic Regression model, and saves it as model.pkl
# ============================================================

import pandas as pd                          # For loading and working with data
from sklearn.linear_model import LogisticRegression  # Our ML model
from sklearn.model_selection import train_test_split  # To split data into train/test
from sklearn.preprocessing import StandardScaler      # To scale our features (NEW!)
from sklearn.metrics import accuracy_score, classification_report
import pickle                                # To save the trained model to a file
import os

# ---- Step 1: Load the dataset ----
# We expect the CSV file to be in the ../dataset/ folder
dataset_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'BankChurn.csv')

print("Loading dataset...")
df = pd.read_csv(dataset_path)

print(f"Dataset loaded! Shape: {df.shape}")
print(f"Columns available: {list(df.columns)}")

# ---- Step 2: Select only the columns we need ----
# We use only Age, Balance, CreditScore as input features
# 'Exited' is our target column (1 = churned, 0 = stayed)
features = ['Age', 'Balance', 'CreditScore']
target   = 'Exited'

X = df[features]   # Input features (what we feed into the model)
y = df[target]     # Target label (what we want to predict)

print(f"\nFeatures (X): {features}")
print(f"Target (y): {target}")
print(f"Class distribution:\n{y.value_counts()}")

# ---- Step 3: Split data into training and testing sets ----
# 80% of data goes to training, 20% for testing
# random_state=42 means the split is reproducible (same every run)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining samples : {len(X_train)}")
print(f"Testing  samples : {len(X_test)}")

# ---- Step 4: Scale the features (NEW!) ----
# Logistic Regression is sensitive to feature scaling.
# Since Balance (0-200k) is much larger than Age (18-90), we MUST scale them.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

print("\nFeatures scaled successfully!")

# ---- Step 5: Train the Logistic Regression model ----
# We use class_weight='balanced' because our dataset is imbalanced (80/20)
print("\nTraining Logistic Regression model...")
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train_scaled, y_train)

# ---- Step 6: Evaluate the model ----
y_pred    = model.predict(X_test_scaled)
accuracy  = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ---- Step 7: Save the model AND the scaler ----
# We MUST save the scaler because we need to apply the SAME scaling
# to any new customer data that comes into the API.
model_path  = os.path.join(os.path.dirname(__file__), 'model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(model, f)

with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

print(f"\nModel saved successfully to: {model_path}")
print(f"Scaler saved successfully to: {scaler_path}")
print("\n✅ Training complete! You can now start the FastAPI server.")
