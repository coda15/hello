import streamlit as st
from io import StringIO
import os
import assemblyai as aai

# title and favicon ------------------------------------------------------------

st.set_page_config(page_title="Speech to Text Transcription App", page_icon="👄")

# _max_width_()

# logo and header -------------------------------------------------

st.text("")
st.image(
    "https://emojipedia-us.s3.amazonaws.com/source/skype/289/parrot_1f99c.png",
    width=125,
)

st.title("Speech to text transcription app")

uploaded_file = st.file_uploader("Choose a mp3 file", type=["mp3"])


def hello():
    aai.settings.api_key = "64ad0625eb954f83b1c465e0458415b6"

    transcriber = aai.Transcriber()

    audio_url = (
        "audio_2.mp3"
    )

    config = aai.TranscriptionConfig(speaker_labels=True)

    transcript = transcriber.transcribe(audio_url, config)

    print(transcript.text)

    for utterance in transcript.utterances:
        return utterance.speaker, utterance.text
    
    # return transcript.text

if uploaded_file is not None:
    st.write(hello())