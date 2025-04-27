import yt_dlp

def download_youtube_video(url):
    ydl_opts = {
        'outtmpl': 'downloaded_video.mp4',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

