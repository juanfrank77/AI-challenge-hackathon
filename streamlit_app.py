import streamlit as st
import whisper
from audiorecorder import audiorecorder

st.title("Team Tonic Demo")

st.write("Take a picture first and speak your request for the model")

image = st.camera_input("Take a picture")

audio = audiorecorder("Click to record", "Click to stop recording")

## model = whisper.load_model("base")
## st.text("Whisper Model Loaded")

if audio is not None:
    st.audio(audio.export().read())

    submit_button = st.button("Submit request")

    st.info("Working...")

"""
    result = model.transcribe(audio)

    st.success("Transcription complete")
    st.markdown(result['text'])

else:
    st.error("Please record your request...")
"""
