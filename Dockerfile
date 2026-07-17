# Use a slim Python image
FROM python:3.11-slim

# Install system dependencies (Updated to use 'libgl1')
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY . .

# Command to run your app
CMD ["streamlit", "run", "app.py"]