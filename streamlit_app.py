import streamlit as st
from audiorecorder import audiorecorder
from gradio_client import Client
import whisper

st.title("Team Tonic Demo")

st.subheader("Take a picture first and speak your request for the model")

image = st.camera_input("Camera input")

audio = audiorecorder("Click to record audio", "Click to stop recording")

client = Client("https://ysharma-llava-v1.hf.space/--replicas/5hq2h/")

if len(audio) > 0:
    st.audio(audio)

    submit_button = st.button("Use this audio")

    if submit_button:
            
        st.info("Transcribing...")

        
        st.success("Transcription complete")
        with st.expander("See transcript"):
            st.markdown("Here goes the result")

        st.text("Sending image and request to the model. Please wait...")
       # result = client.predict(
       #     result['text'],
       #     image,
       #     "Crop",
       #     fn_index=7
       # )
       # print(result)
