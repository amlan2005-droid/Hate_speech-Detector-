from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="cardiffnlp/twitter-roberta-base-offensive"
)

def get_hate_score(text):
    prediction = classifier(
        text,
        truncation=True,
        max_length=512
    )
    return prediction