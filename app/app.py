#!/usr/bin/env python3
from flask import Flask, request, jsonify
from app.model import analyze_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    response = {
        "message": "Welcome to Michael Claus' Sentiment Analysis API!",
        "author": {
            "name": "Michael Claus",
            "linkedin": "https://www.linkedin.com/in/mclausaudio/"
        },
        "instructions": {
            "endpoint": "/sentiment",
            "method": "POST",
            "description": "To analyze sentiment, make a POST request to /sentiment with the text as JSON data.",
            "example_request_body": {
                "text": "This is the text you want to analyze."
            }
        }
    }
    return jsonify(response)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.json
    input_text = data.get('text', '')

    if not input_text:
        return jsonify({"error": "Text is missing"}), 400

    sentiment_label = analyze_sentiment(input_text)
    return jsonify({"sentiment": sentiment_label})

@app.errorhandler(404)
def not_found(error):
    response = {
        "error": "Route not found",
        "available_routes": [
            {
                "route": "/",
                "methods": ["GET"],
                "description": "Welcome message and instructions"
            },
            {
                "route": "/sentiment",
                "methods": ["POST"],
                "description": "Analyze sentiment of the given text"
            }
        ]
    }
    return jsonify(response), 404

if __name__ == '__main__':
    app.run(debug=True)