import streamlit as st
import pytesseract
import cv2
import requests
import json
import moviepy.editor as mp
from pdf2image import convert_from_path
import numpy as np
import speech_recognition as sr

# Set up Streamlit app
st.title("Media to Text Summarization")
st.sidebar.title("Upload Options")

OPENROUTER_API_KEY = "your_api_key"

# API function
def query_qwen_api(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "qwen/qwen-2-vl-72b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": 0.7,
        "top_p": 1,
    }
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        data=json.dumps(payload),
    )
    if response.status_code == 200:
        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return "No valid response from the API."
    else:
        return f"Error: {response.status_code} - {response.text}"

# Media processing functions
def image_to_text(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text if text else "No text found in the image."

def pdf_to_text(pdf_path):
    pages = convert_from_path(pdf_path, 300)
    text = ""
    for page in pages:
        img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)
        text += pytesseract.image_to_string(img)
    return text if text else "No text found in the PDF."

def video_to_audio(video_path):
    video = mp.VideoFileClip(video_path)
    audio_file = "extracted_audio.wav"
    video.audio.write_audiofile(audio_file)
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        return recognizer.recognize_google(audio)

# Streamlit user interface
uploaded_file = st.sidebar.file_uploader("Upload Image, PDF, or Video", type=["pdf", "jpg", "png", "mp4"])

if uploaded_file:
    file_name = uploaded_file.name.lower()

    if file_name.endswith('.pdf'):
        with st.spinner("Processing PDF..."):
            pdf_text = pdf_to_text(uploaded_file)
            st.subheader("Extracted Text from PDF")
            st.write(pdf_text)
    elif file_name.endswith(('.jpg', '.png')):
        with st.spinner("Processing Image..."):
            image_text = image_to_text(uploaded_file)
            st.subheader("Extracted Text from Image")
            st.write(image_text)
    elif file_name.endswith('.mp4'):
        with st.spinner("Processing Video..."):
            audio_text = video_to_audio(uploaded_file)
            st.subheader("Extracted Text from Video Audio")
            st.write(audio_text)
    else:
        st.error("Unsupported file format!")


