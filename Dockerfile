# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies for Pygame
RUN apt-get update && apt-get install -y \
    python3-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    libportmidi-dev \
    libavformat-dev \
    libswscale-dev \
    libjpeg-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir .

# Command to run the game (will fail without a display)
CMD ["python", "src/main.py"]
