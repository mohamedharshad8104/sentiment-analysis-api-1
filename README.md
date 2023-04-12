# Sentiment Analysis API
by Michael Claus

This repository contains the code for a sentiment analysis API built using Python, Flask, Hugging Face's Transformers library, Docker, and deployed on AWS. The API utilizes a pre-trained model to classify input text as positive, negative, or neutral.

https://github.com/mclausaudio/sentiment-analysis-api/blob/main/README/sentiment-analysis-api-demo-michael-claus-480.mov?raw=true

## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or higher
- Docker

### Installation
Clone the repository: `git clone https://github.com/yourusername/sentiment-analysis-api.git`
Change to the project directory: `cd sentiment-analysis-api`
Create a virtual environment and activate it: `python -m venv venv`

Install the required packages: `pip install -r requirements.txt`
Run the Flask app locally: `export FLASK_APP=app/app.py && flask run`

Now you can access the API http://localhost:5000 on your local machine.

### Building and Running the Docker Container
Build the Docker container: `docker build -t sentiment-analysis-api .`
Run the Docker container: `docker run -p 8080:80 sentiment-analysis-api`

Now you can access the API at http://localhost:8080 on your local machine.

## Usage
To use the API, make a POST request to the /analyze endpoint with the following JSON payload:
```
{
  "text": "your text here"
}
```

The API will return a JSON object with the sentiment classification:
```
{
  "sentiment": "positive"
}
```

License
This project is licensed under the MIT License - see the LICENSE file for details.