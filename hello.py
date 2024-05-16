import streamlit as st
import pandas as pd
import whisper as wh
from io import StringIO
from openai import OpenAI
import os
import assemblyai as aai


# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

uploaded_file = st.file_uploader("Choose a mp3 file", type=["mp3"])
audio_file= open("audio_2.mp3", "rb")

# if uploaded_file is not None:
#     client = OpenAI(api_key = 'sk-proj-8ErXL4RMyUkLdzsBMxsPT3BlbkFJTOPo8FmiRqa0iBWzbygm')

#     transcription = client.audio.transcriptions.create(
#         model="whisper-1", 
#         file=audio_file,
#         response_format="text"
#     )
#     print(transcription.text)


aai.settings.api_key = "64ad0625eb954f83b1c465e0458415b6"

transcriber = aai.Transcriber()

audio_url = (
    "audio_2.mp3"
)

config = aai.TranscriptionConfig(speaker_labels=True)

transcript = transcriber.transcribe(audio_url, config)

print(transcript.text)

for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")