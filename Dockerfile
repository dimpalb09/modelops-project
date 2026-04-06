# ============================================================
# Dockerfile
# This file tells Docker how to build our backend container
# ============================================================

# Step 1: Use an official Python 3.11 image as our base
FROM python:3.11-slim

# Step 2: Set a working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file first
# (Doing this before copying all code means Docker caches the pip install layer)
COPY requirements.txt .

# Step 4: Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all backend files into the container
COPY . .

# Step 6: Copy the dataset folder (needed for training inside Docker if wanted)
# Note: model.pkl must already be trained and copied here before build
# OR you can train inside Docker by running: python train_model.py

# Step 7: Expose port 8000 so Docker maps it to your computer
EXPOSE 8000

# Step 8: Command to start the FastAPI server using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# ---- How to build and run ----
# docker build -t modelops-api .
# docker run -p 8000:8000 modelops-api
