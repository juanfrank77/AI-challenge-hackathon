import streamlit as st
from audio2numpy import open_audio
from st_audiorec import st_audiorec
from gradio_client import Client
import whisper

st.title("Team Tonic Demo")
st.subheader("Take a picture first and speak your request for the model")

image = st.camera_input("Camera input")

audio_data = st_audiorec()

model = whisper.load_model("base")

client = Client("https://ysharma-llava-v1.hf.space/--replicas/5hq2h/")

if audio_data is not None:
    st.audio(audio_data, format='audio/wav')

    submit_button = st.button("Use this audio")

    if submit_button:
        signal, _ = open_audio(audio_data)
        result = model.transcribe(signal)
        st.info("Transcribing...")
        
        st.success("Transcription complete")
        transcript = result['text']
        
        with st.expander("See transcript"):
            st.markdown(transcript)

        st.text("Sending image and request to the model. Please wait...")
       # result = client.predict(
       #     transcript,
       #     image,
       #     "Crop",
       #     fn_index=7
       # )
       # print(result)
