from fastapi import FastAPI
from pydantic import BaseModel
import pdfkit
from jinja2 import Template
import uvicorn

# Set the path to wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

# Convert an HTML string to PDF
# pdfkit.from_string("<h1>Hello, PDF!</h1>", "output.pdf", configuration=config)

# User interaction through API
# Resume data collection
# PDF generation

# Initialize FastAPI
app = FastAPI()

# User input schema
class ResumeData(BaseModel):
    name: str
    email: str
    phone: str
    skills: list
    experience: list
    education: list
    summary: str

# HTML Template for Resume
resume_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Resume</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #2E86C1; }
        h2 { border-bottom: 2px solid #2E86C1; }
        p { margin: 5px 0; }
    </style>
</head>
<body>
    <h1>{{ name }}</h1>
    <p><strong>Email:</strong> {{ email }}</p>
    <p><strong>Phone:</strong> {{ phone }}</p>
    <h2>Summary</h2>
    <p>{{ summary }}</p>
    <h2>Skills</h2>
    <ul>
        {% for skill in skills %}
        <li>{{ skill }}</li>
        {% endfor %}
    </ul>
    <h2>Experience</h2>
    <ul>
        {% for job in experience %}
        <li>{{ job }}</li>
        {% endfor %}
    </ul>
    <h2>Education</h2>
    <ul>
        {% for edu in education %}
        <li>{{ edu }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# API Endpoint: Generate Resume
@app.post("/generate_resume")
async def generate_resume(data: ResumeData):
    # Render template
    template = Template(resume_template)
    resume_html = template.render(
        name=data.name, email=data.email, phone=data.phone, 
        skills=data.skills, experience=data.experience, 
        education=data.education, summary=data.summary
    )
    
    # Convert to PDF
    pdf_filename = "resume.pdf"
    pdfkit.from_string(resume_html, pdf_filename,configuration=config)

    return {"message": "Resume generated successfully!", "file": pdf_filename}

# Run API
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)