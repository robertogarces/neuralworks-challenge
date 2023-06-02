# Use the official Python image as the base image
FROM python:3.8.13-slim-buster

# Set the working directory
WORKDIR /main

COPY requirements.txt .

ADD Flask ./Flasj
# Install the required packages
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the working directory
COPY main.py .
COPY model/lgbm_model_late_flight_v1.pkl model/
COPY utils/ utils/

EXPOSE 8081

# Start the app using the uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]