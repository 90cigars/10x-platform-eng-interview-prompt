# Use the official Python image from Docker Hub
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python application and requirements file to the container
COPY app.py .
COPY seattle-weather.csv .
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port that the Flask app will run on
EXPOSE 5000

# Define the command to run when the container starts
CMD ["python", "app.py"]
