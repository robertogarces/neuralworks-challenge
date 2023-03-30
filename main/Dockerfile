# Use the official Python image as the base image
FROM python:3.8.13-slim-buster

# Set the working directory
WORKDIR /main

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the working directory
COPY main.py .
COPY model/lgbm_model_late_flight_v1.pkl model/
COPY model/lgbm_model_late_flight_v1.txt model/
COPY utils/ utils/

# Expose the app port
EXPOSE 8000

# Start the app using the uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]