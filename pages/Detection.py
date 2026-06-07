import streamlit as st
import time

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Detection | AI Hate Speech Detector",
    page_icon="🎯",
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
    padding: 35px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.8));
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 10px 40px rgba(0, 229, 255, 0.1);
    margin-bottom: 25px;
    transition: transform 0.3s ease;
}

.hero-box:hover {
    transform: translateY(-2px);
    border: 1px solid rgba(0, 229, 255, 0.3);
}

.section-box {
    background: rgba(20, 27, 45, 0.6);
    backdrop-filter: blur(8px);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    margin-top: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.result-card {
    background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.8));
    backdrop-filter: blur(10px);
    padding: 24px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    margin-top: 24px;
    transition: transform 0.3s ease;
}

.result-card:hover {
    transform: translateY(-5px);
    border: 1px solid rgba(0, 229, 255, 0.3);
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
<div class="hero-box">

# 🎯 Hate Speech Detection

Upload audio or video files and let the AI pipeline:
- Transcribe speech
- Translate Hinglish/Hindi
- Detect offensive content
- Generate moderation insights

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MEDIA INPUT
# ---------------------------------------------------

st.subheader("📂 Upload Media or Paste Link")

uploaded_file = st.file_uploader(
    "Supported formats: MP3, WAV, MP4",
    type=["mp3", "wav", "mp4"]
)

link = st.text_input(
    "Paste YouTube / Social Media Link"
)

# ---------------------------------------------------
# FILE PREVIEW
# ---------------------------------------------------

import os
from Backend.Services.link_downloader import download_video
from Backend.Services.video_processor import convert_to_wav
from Core.fusion_layer import analyze_content

if uploaded_file or link:
    if uploaded_file:
        st.success("✅ File uploaded successfully!")
        file_type = uploaded_file.type

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("""
            <div class="section-box">
            <h3>🎵 Media Preview</h3>
            </div>
            """, unsafe_allow_html=True)

            if "audio" in file_type:
                st.audio(uploaded_file)
            elif "video" in file_type:
                st.video(uploaded_file)

        with col2:
            st.markdown("""
            <div class="section-box">
            <h3>📄 File Information</h3>
            </div>
            """, unsafe_allow_html=True)

            st.write(f"**Filename:** {uploaded_file.name}")
            st.write(f"**Type:** {uploaded_file.type}")
            st.write(f"**Size:** {round(uploaded_file.size / (1024 * 1024), 2)} MB")
    else:
        st.success("✅ Link received!")

    # ---------------------------------------------------
    # DETECTION BUTTON
    # ---------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Run AI Detection"):
        progress_bar = st.progress(0)
        status = st.empty()

        status.info("🎙️ Preparing media...")
        progress_bar.progress(10)

        input_path = ""
        if uploaded_file:
            os.makedirs("temp", exist_ok=True)
            input_path = os.path.join("temp", uploaded_file.name)
            with open(input_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
        elif link:
            input_path = download_video(link)

        status.info("🎙️ Extracting audio...")
        progress_bar.progress(30)
        audio_path = convert_to_wav(input_path)

        status.info("🧠 Running AI Pipeline (Whisper, Translation, Hate Detection)...")
        progress_bar.progress(60)
        
        result = analyze_content(audio_path)
        
        progress_bar.progress(100)
        status.success("✅ Analysis Complete!")

        # ---------------------------------------------------
        # RESULTS SECTION
        # ---------------------------------------------------

        st.markdown("""
        <div class="result-card">
        <h2>🧠 Detection Results</h2>
        </div>
        """, unsafe_allow_html=True)

        metric1, metric2, metric3 = st.columns(3)

        hate_prob = 0.0
        prediction_label = "Neutral"
        pred_data = result["prediction"]
        if isinstance(pred_data, list) and len(pred_data) > 0:
            pred_item = pred_data[0]
            if pred_item["label"] == "LABEL_1":
                hate_prob = pred_item["score"]
                prediction_label = "Offensive"
            else:
                hate_prob = 1.0 - pred_item["score"]
                prediction_label = "Safe"

        with metric1:
            st.metric("Offensive Score", f"{round(hate_prob * 100, 2)}%")

        with metric2:
            st.metric("Toxicity Level", prediction_label)

        with metric3:
            st.metric("Language", "Detected (Auto)")

        # ---------------------------------------------------
        # TRANSCRIPT
        # ---------------------------------------------------

        st.markdown("---")
        st.subheader("📝 Transcript")
        st.text_area("Generated Transcript", value=result["transcript"], height=180)

        # ---------------------------------------------------
        # TRANSLATION
        # ---------------------------------------------------

        st.subheader("🌐 English Translation")
        st.text_area("Translated Text", value=result["translated_text"], height=180)

        # ---------------------------------------------------
        # FINAL DECISION
        # ---------------------------------------------------

        st.subheader("⚖️ AI Moderation Decision")

        if hate_prob > 0.5:
            st.error(f"⚠️ Offensive language detected.\n\nReason: The pipeline has detected offensive or toxic content with {round(hate_prob*100, 1)}% confidence.")
        else:
            st.success("✅ Content appears to be safe.\n\nReason: No significant harmful patterns were detected.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
AI Hate Speech Detection System • Streamlit UI
</div>
""", unsafe_allow_html=True)