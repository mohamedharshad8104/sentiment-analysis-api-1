# Use an official Python runtime as a parent image
FROM public.ecr.aws/docker/library/python:3.10-slim

# Set the working directory to /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask_cors
COPY . .
EXPOSE 5000
CMD ["python", "-m", "app.app"]


# Define environment variable
ENV PYTHONPATH=/app
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py when the container launches
# CMD ["flask", "run", "--port", "80"]
CMD ["gunicorn", "app.app:app", "-w", "4", "-t", "300", "-b", "0.0.0.0:80"]
# This command tells Gunicorn to start 4 worker processes (-w 4), bind to all available network interfaces on port 80 (-b 0.0.0.0:80), and run your Flask app from the app.app module (app.app:app).
