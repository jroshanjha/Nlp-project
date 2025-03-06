from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
import re
import spacy
import gensim
from gensim import corpora
import nltk
from nltk.corpus import stopwords
import string
import uvicorn
# python -m spacy download en_core_web_sm

# Download necessary NLP tools
nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")

# Create a FastAPI application object 
# Initialize FastAPI
app = FastAPI()

# Stopwords for filtering
stop_words = set(stopwords.words("english"))

# Sample financial text corpus
documents = [
    "Stock market is experiencing a major crash due to economic instability.",
    "Investors are looking for safer assets like gold and bonds.",
    "Tech stocks like Apple and Google are showing strong growth trends.",
    "Cryptocurrency adoption is increasing despite regulatory concerns.",
    "Federal Reserve interest rate hike impacts the banking sector."
]

# Function to clean and preprocess text
# text = re.sub(r'\W+', ' ', text)  # Remove all special characters
# text = re.sub(r'[^a-zA-Z\s]', ' ', text)  # Keep only letters and spaces
# text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
# text = text.sub(r'\d+', ' ', text) # Remove digits
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W+\d+\s+', ' ', text)  # Remove special characters
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    text = " ".join([word for word in text.split() if word not in stop_words]) # remove stop words
    return text

# Preprocess documents
processed_docs = [preprocess_text(doc) for doc in documents]
tokenized_docs = [doc.split() for doc in processed_docs]

# Create a dictionary and corpus
dictionary = corpora.Dictionary(tokenized_docs)
corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]

# Train LDA model
# Topic Modeling Application using Latent Dirichlet Allocation (LDA)
lda_model = gensim.models.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=10) # 3 topics


# API Input Schema
class TextData(BaseModel):
    text: str
    

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# API Endpoint: Get Topics from Text
@app.post("/extract_topics")
async def extract_topics(data: TextData):
    text = preprocess_text(data.text)
    bow_vector = dictionary.doc2bow(text.split())
    topics = lda_model.get_document_topics(bow_vector)

    # Get topic names from LDA model
    topic_list = []
    for topic_id, probability in topics:
        topic_words = lda_model.show_topic(topic_id, topn=5)  # Get top words for each topic
        topic_name = ", ".join([word for word, _ in topic_words])  # Create a name from top words

        topic_list.append({
            "topic_id": int(topic_id),
            "topic_name": topic_name,
            "probability": float(probability)
        })

    return {"topics": topic_list}
    # return jsonable_encoder({"topics": topic_list})
# async def extract_topics(data: TextData):
#     text = preprocess_text(data.text)
#     bow_vector = dictionary.doc2bow(text.split())
#     topics = lda_model.get_document_topics(bow_vector)
    
#     # Format topics
#     topic_list = [{"topic_id": topic[0], "probability": topic[1]} for topic in topics]
#     return {"topics": topic_list}

# Run API (use `uvicorn topic_modeling:app --reload` to start)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # localhost
    
    
# http://127.0.0.1:8000/extract_topics

# eg -- The stock market is fluctuating due to interest rate hikes


# Finance and Economics 
# The Federal Reserve increased interest rates, affecting the stock market and bond yields.

# Technology and AI 
# The rise of artificial intelligence has transformed industries, including finance and banking.
# OpenAI has launched a new GPT model that improves natural language understanding and text generation.

# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.

# Cryptocurrency and Blockchain
# Cryptocurrency has become a popular method of payment, with more than 10% of the global market cap.
# The rise of cryptocurrency has led to the development of blockchain technology, which is being used in various
# applications, including supply chain management and voting systems.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.
# The model is being used in various applications, including chatbots and virtual assistants.

# Sports
# The Champions League final between Real Madrid and Manchester City was intense, with extra-time drama.
# The 2024 Olympics are being held in Paris, with athletes from around the world competing in
# various events.

# Politics
# The 2024 US presidential election is being held, with candidates from both parties vying for
# the top spot.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.


# Healthcare and Medicine
# A new study reveals that exercise and a balanced diet can significantly reduce the risk of heart disease.
# The COVID-19 pandemic has caused a global health crisis, with millions of people affected.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.

# 📌 Movies & Entertainment
# Christopher Nolan’s latest film explores time travel and complex storytelling, featuring an all-star cast.
# The new Marvel movie has broken box office records, with fans worldwide eagerly awaiting the next installment.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.

# 📌 Politics
# The 2024 US presidential election is being held, with candidates from both parties vying for
# the top spot.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.

# 📌 Sports
# The Champions League final between Real Madrid and Manchester City was intense, with extra-time drama.
# The 2024 Olympics are being held in Paris, with athletes from around the world competing in
# various events.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.


# 📌 Technology
# The rise of artificial intelligence has transformed industries, including finance and banking.
# OpenAI has launched a new GPT model that improves natural language understanding and text generation.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.


# 📌 Travel
# The new travel app has made it easier for users to book flights and hotels.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.

# 📌 Weather
# The weather forecast for the next week is expected to be mostly sunny, with temperatures in the mid
# 60s.
# The model is being used in various applications, including chatbots and virtual assistants.
# The model's capabilities have sparked interest in the field of natural language processing.
# The model's potential applications are vast, including customer service and content creation.
# The model's limitations are also being explored, including bias and accuracy.
# The model's impact on society is being studied, including job displacement and privacy concerns.