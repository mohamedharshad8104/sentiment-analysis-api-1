from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "finiteautomata/bertweet-base-sentiment-analysis"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Model and tokenizer downloaded successfully.")