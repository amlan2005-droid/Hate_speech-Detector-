from Core.preprocessing import preprocess_for_slang

# -----------------------------
# LOAD SLANG WORDS (.txt)
# -----------------------------

slang_words = set()

with open("notebooks/data/slang_words.txt", "r", encoding="utf-8") as f:
    for line in f:
        word = line.split("-")[0].strip().lower()
        if word:
            slang_words.add(word)

# Short slang handled separately
SHORT_SLANG = {"mc", "bc", "bsdk", "stfu", "gtfo", "mf", "kys", "tf"}


# -----------------------------
# SLANG SCORE FUNCTION
# -----------------------------

def get_slang_score(text: str) -> float:
    words = preprocess_for_slang(text)
    full_text = " ".join(words)

    total_weight = 0
    max_weight = 0

    # short slang
    for word in words:
        if word in SHORT_SLANG:
            total_weight += 0.8
            max_weight = max(max_weight, 0.8)

    # long slang
    for slang in slang_words:
        occurrences = full_text.count(slang)
        if occurrences > 0:
            total_weight += occurrences * 1.0
            max_weight = max(max_weight, 1.0)

    if not words:
        return 0.0

    density = total_weight / len(words)

    # 🔥 combine intensity + density
    final_score = 0.6 * density + 0.4 * max_weight

    return min(final_score, 1.0)