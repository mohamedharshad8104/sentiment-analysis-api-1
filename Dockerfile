# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt. The --trusted-host pypi.python.org flag tells pip that it can trust the pypi.python.org host, which is the default package index for Python packages.
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Download the model and tokenizer
RUN python download_model.py

# Make port 80 available to the world outside this container
# This line tells Docker that your container will expose port 80, which means that this port will be available for connections from the outside world. Port 80 is the default HTTP port, and by exposing it, you are making your API accessible on this port. When you run the container, you can map this port to another port on your host machine if you prefer, but by default, your API will listen on port 80 inside the container.
EXPOSE 80

# Define environment variable
ENV PYTHONPATH=/app
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py when the container launches
# CMD ["flask", "run", "--port", "80"]
CMD ["gunicorn", "app.app:app", "-w", "4", "-t", "300", "-b", "0.0.0.0:80"]
# This command tells Gunicorn to start 4 worker processes (-w 4), bind to all available network interfaces on port 80 (-b 0.0.0.0:80), and run your Flask app from the app.app module (app.app:app).