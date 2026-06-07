import re

# -----------------------------
# BASIC CLEANING (for ML model)
# -----------------------------

def clean_text(text: str) -> str:
    """
    Cleans text for TF-IDF / ML model
    """
    text = str(text).lower()

    # remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # remove mentions (@user)
    text = re.sub(r'@\w+', '', text)

    # remove hashtags but keep words
    text = re.sub(r'#(\w+)', r'\1', text)

    # remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# -----------------------------
# NORMALIZATION (for slang)
# -----------------------------

def normalize_text(text: str) -> str:
    """
    Strong normalization for slang detection
    Handles repeated characters and messy input
    """
    text = str(text).lower()

    # remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # collapse repeated letters (e.g. chutiyaaa → chutiya)
    text = re.sub(r'(.)\1+', r'\1', text)

    return text


# -----------------------------
# TOKENIZATION
# -----------------------------

def tokenize(text: str):
    """
    Simple tokenizer (space-based)
    """
    return text.split()


# -----------------------------
# PIPELINES (used by layers)
# -----------------------------

def preprocess_for_model(text: str) -> str:
    """
    Pipeline for ML model input
    """
    return clean_text(text)


def preprocess_for_slang(text: str):
    """
    Pipeline for slang detection
    """
    text = normalize_text(text)
    return tokenize(text)