# Nlp-project
This  Repository represent by how Text preprocessing and Analytics Text .

# Create Environment Variables 
conda create -p venv python==3.11 -y
python -m venv new_venv

# Activate Environment Variables 
conda activate venv/
new_venv\Scripts\activate

# installment Requirements Library
pip install -r requirements.txt

# Procfile
web: python app.py
web: streamlit app.py

# Run Project
streamlit run app.py
python run app.py  ( python app.py)

* Running on http://127.0.0.1:5000
* Running on http://192.168.1.5:5000

# Project Structure
flask-applications/
├── app.py
├── app.log
├── static/
│   ├── js/
│   │   ├── api.js
│   │   └── app.js
│   └── css/
│       └── custom.css (optional)
├── templates/
│   ├── base.html
│   ├── index.html
│   └── product_form.html
├── migrations/
├── requirements.txt
└── venv/

# Server 
http://127.0.0.1:5000/


flask db init     # Initialize migrations (first time only)
flask db migrate  # Generate migration script
flask db upgrade  # Apply migrations to the database

mysql -u root -p
USE product_db;
SHOW TABLES;

## Docker runs with the following
docker build -t jroshan731/welcome-app .
docker images 


## Run Dockers
docker run -p 5000:5000 welcome-app

## docker port , host
docker psc

## push docker image into docker container
docker login ( jroshan123)

docker image rm -f topic-modeling 

# rename 
docker tag jroshan123/welcome-app jroshan123/topic-modeling

# push 
docker push jroshan123/welcome-app1
docker push jroshan123/topic-modeling:lates

docker pull jroshan123/topic-modeling:latest

docker run -d -p 8080:8080 jroshan123/topic-modeling:latest



# Topics Modeling 
# 1. Text Preprocessing
# 2. Vectorization
# 3. Model Selection
# 4. Model Training
# 5. Model Evaluation
# 6. Model Deployment
# 7. Model Interpretation
# 8. Model

Topic Modeling Application using Latent Dirichlet Allocation (LDA) with FastAPI for deployment. This app will analyze financial news/articles and extract topics automatically.

🚀 Features of the Application
✅ Preprocess text (cleaning, tokenization, stopwords removal)
✅ Extract topics from financial news/articles using LDA
✅ Deploy API using FastAPI
✅ Interactive UI (optional: Streamlit for visualization)


2️⃣ Build the Topic Modeling App (FastAPI)
This script includes:

Text preprocessing
LDA Model for Topic Extraction
API Endpoints

3️⃣ How It Works
✅ Preprocesses text (removes noise, tokenizes)
✅ LDA extracts topics from financial articles
✅ API endpoint (/extract_topics) returns topic probabilities


uvicorn app:app --reload

🔥 Verify Installation Inside Docker
Run the container interactively:
docker run -it your-container-name bash

Check installed models
python -m spacy validate


# Machine Translation 
🚀 Features of the Application
✅ Translate text between multiple languages
✅ Use a pre-trained Transformer model (MarianMT)
✅ Deploy as an API with FastAPI
✅ Interactive UI (optional: Streamlit for web interface)

Next Steps
🔥 Extend to More Languages → Add support for Hindi, Chinese, Japanese, Arabic, etc.
📊 Add a Web UI → Use Streamlit to make an interactive front-end.
🚀 Deploy on Cloud → Containerize with Docker and host on AWS/GCP.
🚀

🚀 Features of the Application
✅ Classify text sentiment as Positive, Negative, or Neutral
✅ Use a pre-trained Transformer model (DistilBERT for Sentiment Analysis)
✅ Deploy as an API with FastAPI
✅ Optional UI for real-time sentiment analysis (Streamlit)



