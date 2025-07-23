from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
import gradio as gr
from PIL import Image

# BLIP for captions
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# DialoGPT for chat
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

def get_caption(img: Image.Image) -> str:
    img = img.convert("RGB")
    inputs = processor(images=img, return_tensors="pt")
    out_ids = model.generate(**inputs, max_new_tokens=20)
    return processor.decode(out_ids[0], skip_special_tokens=True)

def combined_response(img, message):
    cap = get_caption(img)
    prompt = f"Image shows: {cap}. User says: {message}"
    reply = chatbot(prompt, max_new_tokens=50)[0]["generated_text"]
    return cap, reply.strip()

gr.Interface(
    fn=combined_response,
    inputs=[gr.Image(type="pil"), gr.Textbox(label="Ask something")],
    outputs=["text", "text"],
    title="Smart Assistant with BLIP",
    description="Upload an image, get a caption, and chat about it!",
).launch()
