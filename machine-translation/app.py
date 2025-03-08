'''Build the Machine Translation App (FastAPI)
This script includes:

MarianMT for translation
API endpoint to handle translation requests '''

from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer
import uvicorn
import sentencepiece

# Initialize the FastAPI

app = FastAPI()
# Define the model and tokenizer for MarianMT

# ✅ Correct Model Name
model_name = "Helsinki-NLP/opus-mt-en-hi"

# Supported language pairs (MarianMT models)
language_pairs = {
    "en-fr": "Helsinki-NLP/opus-mt-en-fr",
    "fr-en": "Helsinki-NLP/opus-mt-fr-en",
    "en-es": "Helsinki-NLP/opus-mt-en-es",
    "es-en": "Helsinki-NLP/opus-mt-es-en",
    "en-de": "Helsinki-NLP/opus-mt-en-de",
    "de-en": "Helsinki-NLP/opus-mt-de-en"
}

# Function to load translation model
def load_model(language_pair):
    model_name = language_pairs.get(language_pair)
    if not model_name:
        raise ValueError("Language pair not supported!")
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model


# API Input Schema
class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str
    
@app.get('/')
async def index():
    return {'message': 'Welcome to the Machine Translation API!'}
# API Endpoint: Translate Text
@app.post("/translate")
async def translate_text(request: TranslationRequest):
    language_pair = f"{request.source_lang}-{request.target_lang}"
    
    if language_pair not in language_pairs:
        return {"error": "Translation for this language pair is not supported!"}

    tokenizer, model = load_model(language_pair)
    inputs = tokenizer(request.text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return {"translated_text": translated_text}

# Run API (use `uvicorn machine_translation:app --reload` to start)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)