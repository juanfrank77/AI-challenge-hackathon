import streamlit as st
import numpy as np
from audiorecorder import audiorecorder
from gradio_client import Client
import requests
import base64

st.title("Team Tonic Demo")

st.subheader("Take a picture first and speak your request for the model")

image = st.camera_input("Camera input")

audio = audiorecorder("Click to record audio", "Click to stop recording")

client = Client("https://ysharma-llava-v1.hf.space/--replicas/5hq2h/")

if len(audio) > 0:
    request = audio.export("audio.wav", format="wav")
    
    st.audio(request)

    submit_button = st.button("Use this audio")

    if submit_button:
        with open(request, "rb") as file:
            wav = file.read()
            encoded = base64.b64encode(wav)
            string = encoded.decode("utf-8")

        st.markdown(encoded)
        st.markdown(string)
            
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
