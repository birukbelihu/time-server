# Use Official Python Image
FROM python:3.14.0rc1-slim

# Set Working Directory In Container
WORKDIR /app

# Copy All Project Files To The Container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose The Port
EXPOSE 5000

# Set The Default Command To Run The TimeServer
CMD ["python", "main.py"]
