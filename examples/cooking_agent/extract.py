from moviepy import VideoFileClip


# 1. Extract audio
def extract_audio():
    video_path = "downloaded_video.mp4"
    audio_path = "extracted_audio.wav"
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)


# 2. Transcribe audio

def transcribe_audio_1(client):


    with open("extracted_audio.wav", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe", 
            file=audio_file
        )

    print(transcript.text)
    with open("transcription_output.txt", "w", encoding="utf-8") as f:
        f.write(transcript.text)




