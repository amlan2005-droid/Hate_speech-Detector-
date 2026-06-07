import os
import whisper

# Add ffmpeg to PATH so Whisper can find it
ffmpeg_path = r"D:\ffmpeg-8.1-essentials_build\bin"
if ffmpeg_path not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + ffmpeg_path

model = whisper.load_model("small")

def transcribe_audio(audio_path):
    result = model.transcribe(
        audio_path,
        language="hi",
        fp16=False
    )

    return result["text"]
