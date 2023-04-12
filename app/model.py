# Import the necessary classes from the transformers library
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Specify the name of the pre-trained model
# The model "finiteautomata/bertweet-base-sentiment-analysis" is a pre-trained BERT model, 
# which has been trained on a large corpus of text for masked language modeling and next sentence prediction tasks. 
# This base model is not specifically set up for sentiment analysis.
model_name = "finiteautomata/bertweet-base-sentiment-analysis"

# Load the pre-trained model for sequence classification
# However, when you load the model using AutoModelForSequenceClassification.from_pretrained(model_name), 
# the Hugging Face Transformers library automatically adapts the base BERT model for sequence classification tasks, 
# such as sentiment analysis.
model = AutoModelForSequenceClassification.from_pretrained(model_name)
# The Transformers library handles the necessary modifications to the model architecture
# and provides you with the convenience of using the same model for different tasks, such as sentiment analysis in this case.

# Load the tokenizer associated with the pre-trained model
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define a mapping between class indices and sentiment labels
SENTIMENT_LABELS = {
    0: "negative",
    1: "neutral",
    2: "positive"
}

# Function to preprocess input text
def preprocess(text):
    # Tokenize the input text, pad or truncate it to a fixed length, and convert it to tensors
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    # return_tensors="pt": Return the preprocessed input text as a PyTorch tensor. "pt" stands for PyTorch.
    
    return inputs

# Function to make sentiment predictions
def predict(inputs):
    # Feed the preprocessed inputs into the model and obtain the output logits
    # The output tensor for the adapted BERT model will have the shape [batch_size, num_classes], 
    # where batch_size is the number of input samples processed together, 
    # and num_classes is the number of classes the model is being used for in the specific sequence classification task. 
    # In the case of sentiment analysis, num_classes would be 3, corresponding to negative, neutral, and positive sentiment classes.
    outputs = model(**inputs)
    # Note: the ** operator is used to unpack key-value pairs from a dictionary and pass them as keyword arguments to a function.
    # Similar to spread operator ("..." syntax) in NodeJS
    
    # Find the index of the highest logit (most probable class)
    predicted_class = outputs.logits.argmax(dim=-1).item()
    # So, when using .argmax(dim=-1), you're finding the index of the maximum value along the last dimension (the dimension representing the different sentiment classes) 
    # because the model has been adapted for sequence classification, and this is the standard output structure for such tasks.
    return predicted_class

# Function to interpret the predictions as sentiment labels
def interpret_result(predicted_class: int) -> str:
    # Map the predicted class index to a sentiment label    
    sentiment_label = SENTIMENT_LABELS.get(predicted_class, "unknown")
    return sentiment_label

def analyze_sentiment(input_text):    
    inputs = preprocess(input_text)
    predicted_class = predict(inputs)
    sentiment_label = interpret_result(predicted_class)
    return sentiment_label
