import os
import subprocess

def convert_to_wav(input_file):
    os.makedirs("temp", exist_ok=True)
    output_file = "temp/output.wav"
    ffmpeg_path = "D:\\ffmpeg-8.1-essentials_build\\bin\\ffmpeg.exe"
    
    command = [
        ffmpeg_path,
        "-y",
        "-i", input_file,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        output_file
    ]

    subprocess.run(command, check=True)
    return output_file