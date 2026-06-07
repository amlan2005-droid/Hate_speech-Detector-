import os
from yt_dlp import YoutubeDL

def download_video(url):
    os.makedirs("downloads", exist_ok=True)
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/input.%(ext)s"
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
