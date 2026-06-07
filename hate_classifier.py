from transformers import pipeline

classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-offensive")

def predict_hate(text):
    result = classifier(text)[0]
    return result