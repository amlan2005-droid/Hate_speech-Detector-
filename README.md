# Hate Speech Detection from Text and YouTube Videos

## Overview

This project is an NLP and Machine Learning based Hate Speech Detection system that can analyze text as well as YouTube videos. The system extracts audio from videos using FFmpeg, converts speech into text, preprocesses the text, and classifies it using a TF-IDF vectorizer and a Logistic Regression model.

The goal of this project is to demonstrate an end-to-end AI pipeline for automated content moderation.

---

## Features

* Hate speech detection from text input
* YouTube video URL analysis
* Audio extraction using FFmpeg
* Speech-to-text conversion
* Text preprocessing
* TF-IDF feature extraction
* Logistic Regression based classification
* End-to-end automated pipeline

---

## Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Scikit-learn
* Pandas
* NumPy
* NLTK
* FFmpeg
* Speech Recognition
* Joblib

### Machine Learning

* TF-IDF Vectorization
* Logistic Regression

---

## Project Pipeline

```text
YouTube URL / Text Input
            │
            ▼
   Video Processing
            │
            ▼
FFmpeg Audio Extraction
            │
            ▼
   Speech-to-Text
            │
            ▼
   Text Preprocessing
            │
            ▼
    TF-IDF Vectorizer
            │
            ▼
 Logistic Regression
            │
            ▼
 Hate Speech Prediction
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/hate-speech-detector.git

cd hate-speech-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python app.py
```

For YouTube video analysis:

1. Provide the YouTube video URL.
2. Audio is extracted using FFmpeg.
3. Speech is converted into text.
4. The text is analyzed by the ML model.
5. The prediction result is displayed.

---

## Model

| Component          | Algorithm           |
| ------------------ | ------------------- |
| Feature Extraction | TF-IDF              |
| Classification     | Logistic Regression |

---

## Future Improvements

* Deep Learning models (LSTM/BERT)
* Real-time video stream analysis
* Timestamp-wise hate speech detection
* Confidence score visualization
* REST API with FastAPI
* Docker deployment

---

## Limitations

* Performance depends on speech-to-text quality.
* Context-dependent sarcasm may not be detected.
* Mixed-language conversations may reduce accuracy.
* TF-IDF does not capture deep semantic relationships.

---

## Project Structure

```text
hate-speech-detector/
│
├── data/
├── models/
├── src/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Author

**Amlan Mukherjee**

B.Tech CSE (AI & ML)

---

## License

This project is created for educational and research purposes.
 
