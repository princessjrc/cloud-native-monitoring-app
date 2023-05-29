# This is a Dockerfile for building a Python application image

# Start from the python:3.9-slim-buster base image
FROM python:3.9-slim-buster

# Set the working directory to /app in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all files from the current directory to the working directory in the container
COPY . .

# Set the environment variable FLASK_RUN_HOST to 0.0.0.0 (bind to all network interfaces)
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 for the Flask application
EXPOSE 5000

# Start the Flask application with the "flask run" command
CMD [ "flask", "run" ]
