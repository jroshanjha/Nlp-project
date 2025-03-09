
# 🚀 Build the Speech-to-Text API (FastAPI)
# This script includes:

# Uploading an audio file
# Processing audio with Whisper
# Returning the transcribed text


from fastapi import FastAPI, UploadFile, File
import whisper
import shutil
import os


# Initialize FastAPI
app = FastAPI()

# Load Whisper Model
model = whisper.load_model("base")  # Options: tiny, base, small, medium, large

# API Endpoint: Upload and Transcribe Audio
@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    file_location = f"temp_audio/{file.filename}"
    
    # Save file temporarily
    os.makedirs("temp_audio", exist_ok=True)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Transcribe using Whisper
    result = model.transcribe(file_location)
    
    # Remove temp file
    os.remove(file_location)
    
    return {"transcription": result["text"]}


# Run API (use `uvicorn speech_to_text:app --reload` to start)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)