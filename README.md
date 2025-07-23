
# Smart Assistant Lite (BLIP-powered)

## 🧠 Overview
Smart Assistant Lite is a lightweight AI-powered assistant that combines **image captioning** and **chatbot functionality** into one simple Gradio interface. It uses:

- **BLIP (Bootstrapping Language–Image Pretraining)** by Salesforce for image captioning
- **DialoGPT-small** from Microsoft for chat-based interaction

This version is designed to run on **CPU only** and even works on systems with **4 GB RAM**.

## 🔧 Features
- Upload an image and receive a meaningful caption
- Type a message and get a response considering both the image and your message
- Minimal dependencies and designed to run without GPU

## 📦 Requirements
```bash
pip install gradio transformers pillow
```

## 🚀 Running the App
```bash
python app.py
```

## 📜 License
MIT License © 2025 Hamza Ali
