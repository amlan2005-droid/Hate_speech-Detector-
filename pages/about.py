import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Home | AI Hate Speech Detector",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: transparent;
}

.hero-box {
    padding: 40px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.8));
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 10px 40px rgba(0, 229, 255, 0.1);
    margin-bottom: 30px;
    transition: transform 0.3s ease;
}

.hero-box:hover {
    transform: translateY(-2px);
    border: 1px solid rgba(0, 229, 255, 0.3);
}

.feature-card {
    background: rgba(20, 27, 45, 0.6);
    backdrop-filter: blur(8px);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    height: 220px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-8px);
    background: rgba(30, 41, 59, 0.8);
    border: 1px solid rgba(0, 229, 255, 0.4);
    box-shadow: 0 12px 30px rgba(0, 229, 255, 0.15);
}

.feature-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #00E5FF;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown("""
<div class="hero-box">

# 🛡️ AI Hate Speech Detector

### Smart Moderation System Powered by AI

Detect offensive and toxic content from:
- 🎙️ Audio
- 💬 Text
- 🌐 Social media style language
- 🇮🇳 Hindi + Hinglish speech

This project combines:
Whisper + Translation + NLP Classification + Fusion Logic

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MAIN IMAGE
# ---------------------------------------------------

st.image(
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# FEATURES SECTION
# ---------------------------------------------------

st.subheader("🚀 Core Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🎙️ Audio Transcription
    </div>

    Converts speech into text using OpenAI Whisper.

    ✔ Hindi support  
    ✔ Hinglish support  
    ✔ Podcast / video audio compatible  
    ✔ Noise-tolerant transcription

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🌐 Translation Engine
    </div>

    Automatically translates Hindi/Hinglish
    into English for better NLP analysis.

    ✔ Multilingual workflow  
    ✔ Better classifier compatibility  
    ✔ Improves detection accuracy

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🧠 Offensive Speech Detection
    </div>

    Detects:
    - Hate speech
    - Toxic language
    - Slang abuse
    - Offensive phrases

    Powered by HuggingFace Transformers.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    📊 Analytics Dashboard
    </div>

    Visualize:
    - Hate scores
    - Toxicity trends
    - Speech insights
    - Detection confidence

    Useful for moderation systems.

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# WORKFLOW SECTION
# ---------------------------------------------------

st.markdown("---")

st.subheader("⚙️ System Workflow")

st.code("""
Audio / Text
      ↓
Whisper Transcription
      ↓
Hindi → English Translation
      ↓
Offensive Language Detection
      ↓
Fusion Layer Scoring
      ↓
Final Decision
""")

# ---------------------------------------------------
# PROJECT INSIGHT
# ---------------------------------------------------

st.markdown("---")

st.subheader("💡 Why This Project Matters")

st.write("""
Most hate speech systems fail on:
- Hinglish
- Mixed-language speech
- Internet slang
- Regional abusive phrases

This project tries to bridge that gap using a multi-stage AI pipeline.
""")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
Built with  using Streamlit, Whisper, HuggingFace, and PyTorch
</div>
""", unsafe_allow_html=True)