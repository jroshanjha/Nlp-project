from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

# Text preprocessing
# Sentiment classification using DistilBERT
# API endpoint for real-time analysis

# Initialize FastAPI
app = FastAPI()

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# API Input Schema
class SentimentRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    text = sample_texts = [
        "The stock market is crashing today!",
        "I absolutely love this product! It works perfectly and exceeds all my expectations.",
        "The service was terrible and the staff was rude. Would not recommend.",
        "The movie was okay, nothing special but not bad either.",
        "This restaurant has amazing food and excellent service!",
        "I've had better experiences elsewhere. The pricing is too high for what you get.",
        "Not sure how I feel about this yet, need more time to evaluate.",
        "Best purchase I've made all year! Truly a game-changer.",
        "Disappointing performance and poor build quality.",
        "It's alright, does what it's supposed to do.",
        "Exceptional quality and outstanding customer support. Will definitely buy again!"
    ]
    new_texts = [
        "I can't believe how bad this product is. Complete waste of money.",
        "This new update has some great features that really improve the user experience."
    ]
    return {"message": "Welcome to the Sentiment Analysis API"}

# API Endpoint: Analyze Sentiment
@app.post("/analyze_sentiment")
async def analyze_sentiment(request: SentimentRequest):
    result = sentiment_pipeline(request.text)[0]
    return {"label": result["label"], "confidence": result["score"]}

# Run API (use `uvicorn sentiment_analysis:app --reload` to start)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# How It Works
# ✅ Uses DistilBERT (lightweight version of BERT) for sentiment classification
# ✅ Identifies sentiment as "POSITIVE" or "NEGATIVE" with confidence scores
# ✅ API endpoint (/analyze_sentiment) processes real-time text input