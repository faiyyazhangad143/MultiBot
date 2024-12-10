# MultiBot AI Application

## Overview
MultiBot AI is a versatile, AI-powered application designed to process and summarize a variety of media types, including images, PDFs, audio, and videos. With advanced OCR, speech recognition, and video processing capabilities, it enables users to extract, analyze, and interact with data seamlessly.

## Features
### 1. **Media Processing**
   - **Image Summarization**: Extracts text from images using Tesseract OCR and provides AI-driven summaries.
   - **PDF Summarization**: Converts PDF pages into images, extracts text using OCR, and summarizes the content.
   - **Audio Transcription**: Converts audio files into text using Google Speech Recognition.
   - **Video Analysis**: Extracts audio from video files, transcribes the content, and summarizes the insights.

### 2. **Interactive AI Chatbot**
   - Engage in dynamic conversations with an AI chatbot powered by the Qwen model via the OpenRouter API.
   - Context-aware responses that adapt to the user's queries and chat history.

### 3. **File Upload Support**
   - Handles diverse file formats:
     - **Images**: `.png`, `.jpg`, `.jpeg`, etc.
     - **PDFs**: `.pdf`
     - **Videos**: `.mp4`, `.mov`, `.avi`, etc.
     - **Audio**: `.wav`, `.mp3`, etc.

### 4. **User-Friendly Interface**
   - Built using **Gradio** for an intuitive, web-based UI.
   - Supports file uploads and text inputs seamlessly.

### 5. **Advanced AI Summarization**
   - Leverages the **Qwen AI model** via the OpenRouter API for accurate and concise text summarization.

### 6. **Customizable Deployment**
   - Easily deploy on local machines or hosting platforms like Hugging Face Spaces or Streamlit.

## Requirements
To run this application, ensure the following dependencies are installed:

- **Python 3.7+**
- **Libraries**:
  - `gradio`
  - `pytesseract`
  - `opencv-python`
  - `requests`
  - `moviepy`
  - `pdf2image`
  - `numpy`
  - `SpeechRecognition`
  - `pdfplumber`

### Additional System Requirements
- **Tesseract OCR**: Install the Tesseract binary.
  ```bash
  sudo apt-get install tesseract-ocr
