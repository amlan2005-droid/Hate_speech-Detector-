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

.hero-container {
    padding: 50px;
    border-radius: 25px;
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.8));
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 10px 40px rgba(0, 229, 255, 0.1);
    margin-bottom: 30px;
    transition: transform 0.3s ease;
}

.hero-container:hover {
    transform: translateY(-2px);
    border: 1px solid rgba(0, 229, 255, 0.3);
}

.hero-title {
    font-size: 52px;
    font-weight: bold;
    background: -webkit-linear-gradient(45deg, #00E5FF, #8B5CF6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 22px;
    color: #E2E8F0;
    margin-top: 15px;
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
    margin-bottom: 12px;
    color: white;
}

.section-title {
    font-size: 34px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
    padding-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

st.markdown("""
<div class="hero-container">

<div class="hero-title">
🛡️ AI Hate Speech Detector
</div>

<div class="hero-subtitle">
A modern multilingual AI moderation system for detecting offensive,
toxic, and abusive speech from text and audio.
</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MAIN IMAGE
# ---------------------------------------------------

st.image(
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",
    use_container_width=True
)

# ---------------------------------------------------
# ABOUT SECTION
# ---------------------------------------------------

st.markdown("<div class='section-title'>🚀 Platform Features</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🎙️ Audio Transcription
    </div>

    Convert speech into text using Whisper AI.

    ✔ Hindi support  
    ✔ Hinglish support  
    ✔ Podcast/video audio compatible  
    ✔ Real-world noisy audio handling

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

    ✔ Better classification accuracy  
    ✔ Multilingual moderation support  
    ✔ Transformer-ready output

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="feature-card">

    <div class="feature-title">
    🧠 Offensive Speech Detection
    </div>

    Detect:
    - Hate speech
    - Toxic content
    - Abusive slang
    - Offensive language

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
    - Hate score trends
    - Toxicity distribution
    - Detection statistics
    - AI confidence scores

    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# WORKFLOW
# ---------------------------------------------------

st.markdown("---")

st.markdown("<div class='section-title'>⚙️ System Workflow</div>", unsafe_allow_html=True)

st.code("""
Audio / Text Input
        ↓
Whisper Transcription
        ↓
Hindi → English Translation
        ↓
Transformer-based NLP Detection
        ↓
Fusion Layer Scoring
        ↓
Final Moderation Decision
""")

# ---------------------------------------------------
# PROJECT PURPOSE
# ---------------------------------------------------

st.markdown("---")

st.markdown("<div class='section-title'>💡 Why This Project Matters</div>", unsafe_allow_html=True)

st.info("""
Most existing moderation systems struggle with:
- Hinglish language
- Regional slang
- Mixed-language toxicity
- Audio-based abusive speech

This system attempts to solve that using a complete AI pipeline.
""")

# ---------------------------------------------------
# QUICK STATS
# ---------------------------------------------------

st.markdown("---")

stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:
    st.metric("Languages", "2+")

with stat2:
    st.metric("Detection Types", "4")

with stat3:
    st.metric("AI Models", "3")

with stat4:
    st.metric("Pipeline", "Realtime")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
Built using Streamlit • Whisper • HuggingFace • PyTorch
</div>
""", unsafe_allow_html=True)