from fastapi import FastAPI
from pydantic import BaseModel
from gtts import gTTS
import os

# Text input processing
# TTS conversion using Google TTS (gTTS)
# Returns an MP3 audio file

# Initialize FastAPI
app = FastAPI()

# Request schema
class TTSRequest(BaseModel):
    text: str
    lang: str = "hi"  # Default language is English

# API Endpoint: Convert Text to Speech
@app.post("/text_to_speech/")
async def text_to_speech(request: TTSRequest):
    tts = gTTS(text=request.text, lang=request.lang)
    audio_path = "hindi.mp3"
    tts.save(audio_path)
    
    return {"message": "Audio generated successfully!", "file": audio_path}

# Run API (use `uvicorn text_to_speech:app --reload` to start)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
