from Core.hate_layer import get_hate_score
from Core.slang_layer import get_slang_score
from Core.whisper_layer import transcribe_audio
from Core.translation_layer import translate_text

def analyze_content(audio_path):
    transcript = transcribe_audio(audio_path)
    english_text = translate_text(transcript)
    prediction = get_hate_score(english_text)

    return {
        "transcript": transcript,
        "translated_text": english_text,
        "prediction": prediction
    }

def get_final_result(text: str) -> dict:
    # -----------------------------
    # 1. Get individual scores
    # -----------------------------
    prediction = get_hate_score(text)
    
    hate_score = 0.0
    if prediction and isinstance(prediction, list):
        p = prediction[0]
        if p['label'] == 'LABEL_1': # Offensive
            hate_score = p['score']
        else:
            hate_score = 1.0 - p['score']

    slang_score = get_slang_score(text)      # 0–1

    # -----------------------------
    # 2. Combine (Fusion)
    # -----------------------------
    final_score = 0.7 * hate_score + 0.3 * slang_score

    # -----------------------------
    # 2.5 Rule-Based Boost
    # -----------------------------
    text_lower = text.lower()
    hate_keywords = ["hate", "kill", "destroy"]
    target_keywords = ["community", "people", "religion", "group"]

    rule_boost = 0
    if any(h in text_lower for h in hate_keywords) and any(t in text_lower for t in target_keywords):
        rule_boost = 0.3   # 🔥 boost score
        
    final_score = min(1.0, final_score + rule_boost)

    # -----------------------------
    # 3. Sensitivity Levels
    # -----------------------------
    if final_score < 0.3:
        sensitivity = "LOW"
    elif final_score < 0.6:
        sensitivity = "MEDIUM"
    else:
        sensitivity = "HIGH"

    # -----------------------------
    # 4. Decision
    # -----------------------------
    if final_score * 100 > 70:
        decision = "HATE"
    elif slang_score * 100 > 40:
        decision = "OFFENSIVE"   # 🔥 new category
    else:
        decision = "SAFE"

    # -----------------------------
    # 5. Explanation (VERY IMPORTANT)
    # -----------------------------
    reasons = []

    if hate_score > 0.6:
        reasons.append("Context indicates hate speech")

    if slang_score > 0.4:
        reasons.append("Contains abusive/slang language")

    if not reasons:
        reasons.append("No significant harmful patterns detected")

    # -----------------------------
    # 6. Final Output
    # -----------------------------
    return {
        "text": text,
        "hate_score": float(round(hate_score * 100, 2)),
        "slang_score": float(round(slang_score * 100, 2)),
        "final_score": float(round(final_score * 100, 2)),
        "sensitivity": sensitivity,
        "decision": decision,
        "reason": reasons
    }