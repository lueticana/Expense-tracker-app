# Use Python as base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /uporabniki

# Copy the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "uporabniki.py"]
