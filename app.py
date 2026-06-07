import sys
import os

sys.path.append(os.path.abspath("."))

import streamlit as st
from Core.fusion_layer import get_final_result

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Hate Speech Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: transparent;
}

.stTextArea textarea {
    font-size: 16px;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    background-color: rgba(20, 27, 45, 0.7) !important;
    transition: all 0.3s ease;
}

.stTextArea textarea:focus {
    border-color: #00E5FF !important;
    box-shadow: 0 0 15px rgba(0, 229, 255, 0.2) !important;
}

.result-card {
    padding: 24px;
    border-radius: 20px;
    background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.8));
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    margin-top: 24px;
    transition: transform 0.3s ease;
}

.result-card:hover {
    transform: translateY(-5px);
    border: 1px solid rgba(0, 229, 255, 0.3);
}

.metric-box {
    background: rgba(20, 27, 45, 0.6);
    backdrop-filter: blur(8px);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.05);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.metric-box:hover {
    background: rgba(30, 41, 59, 0.8);
    border: 1px solid rgba(0, 229, 255, 0.4);
    box-shadow: 0 8px 25px rgba(0, 229, 255, 0.15);
}

.big-font {
    font-size: 22px;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:
    st.title("🛡️ AI Moderator")

    st.markdown("---")

    st.write("### Features")
    st.write("✅ Hate Speech Detection")
    st.write("✅ Toxicity Analysis")
    st.write("✅ Slang Detection")
    st.write("✅ AI Fusion Scoring")

    st.markdown("---")

    st.info(
        "This system analyzes user text using "
        "multiple NLP models and fusion scoring."
    )

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🛡️ Hate Speech Detection System")

st.markdown("""
Analyze text using an AI-powered moderation pipeline.

The model checks:
- Offensive language
- Toxicity
- Slang intensity
- Overall risk score
""")

st.markdown("---")

# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------

st.subheader("✍️ Enter Text")

user_input = st.text_area(
    "Type or paste text here",
    height=180,
    placeholder="Example: Enter social media comments, messages, or speech text..."
)

# ---------------------------------------------------
# ANALYZE BUTTON
# ---------------------------------------------------

if st.button("🚀 Analyze Text", use_container_width=True):

    if user_input.strip():

        with st.spinner("Analyzing text with AI models..."):

            result = get_final_result(user_input)

        st.success("Analysis Complete")

        st.markdown("## 📊 Analysis Result")

        # ---------------------------------------------------
        # METRICS
        # ---------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="big-font">🎯 Decision</div>
                <br>
                <h3>{result["decision"]}</h3>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="metric-box">
                <div class="big-font">⚠️ Sensitivity</div>
                <br>
                <h3>{result["sensitivity"]}</h3>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="big-font">📈 Final Score</div>
                <br>
                <h3>{result["final_score"]}</h3>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------------------------------------------------
        # SCORE DETAILS
        # ---------------------------------------------------

        st.markdown("""
        <div class="result-card">
        """, unsafe_allow_html=True)

        st.subheader("📌 Detailed Scores")

        score_col1, score_col2 = st.columns(2)

        with score_col1:
            st.metric(
                label="🔥 Hate Score",
                value=result["hate_score"]
            )

        with score_col2:
            st.metric(
                label="🧠 Slang Score",
                value=result["slang_score"]
            )

        st.markdown("### 📝 Reason")

        st.info(result["reason"])

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter some text before analysis.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
Built with Streamlit • Whisper • HuggingFace • PyTorch
</div>
""", unsafe_allow_html=True)