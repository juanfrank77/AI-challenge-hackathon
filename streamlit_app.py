import streamlit as st
import whisper
from audiorecorder import audiorecorder

st.title("Team Tonic Demo")

st.subheader("Take a picture first and speak your request for the model")

image = st.camera_input("Camera input")

audio = audiorecorder("Click to record audio", "Click to stop recording")

model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if len(audio) > 0:
    st.audio(audio.export().read())

    submit_button = st.button("Submit request")

    if submit_button:
        st.info("Working...")
        
        result = model.transcribe(audio)
        
        st.success("Transcription complete")
        with st.expander("See transcript")
            st.markdown(result['text'])
