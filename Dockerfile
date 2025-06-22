# Base image
FROM arm64v8/python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5001

# Start the Flask serverdocker ps
CMD ["python", "app.py"]
