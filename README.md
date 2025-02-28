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


