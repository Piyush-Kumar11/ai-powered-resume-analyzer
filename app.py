import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from werkzeug.utils import secure_filename
import PyPDF2
from docx import Document

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="resume_analyzer"
)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Read text from PDF files
def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text

# Read text from DOCX files
def read_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Extract skills and user details from resume text
def extract_details_and_skills(resume_text):
    email = None
    phone = None

    # Use regex to find email and phone numbers
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', resume_text)
    phone_match = re.search(r'\b\d{10}\b', resume_text)

    if email_match:
        email = email_match.group(0)

    if phone_match:
        phone = phone_match.group(0)

    # Predefined skills list
    predefined_skills = [
        'Python', 'Java', 'C++', 'JavaScript', 'SQL',
        'HTML', 'CSS', 'Machine Learning', 'Data Analysis',
        'Project Management', 'Communication', 'Teamwork',
        'Leadership', 'Problem Solving'
    ]

    # Initialize skills data
    skills_data = {}

    # Check if each skill is mentioned in the resume text
    for skill in predefined_skills:
        if skill.lower() in resume_text.lower():
            skills_data[skill] = 100  # You can adjust the score logic here

    return {
        "email": email if email else "Not found",
        "phone": phone if phone else "Not found",
        "skills": skills_data
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    name = request.form['name']  # Get the name from the form
    if 'resume' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['resume']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Read resume text based on the file extension
        if filename.lower().endswith('.pdf'):
            resume_text = read_pdf(filepath)
        elif filename.lower().endswith('.docx'):
            resume_text = read_docx(filepath)
        else:
            flash('Unsupported file format.')
            return redirect(url_for('index'))

        # Extract user details and skills
        user_details = extract_details_and_skills(resume_text)
        
        # Save to database
        cursor = db.cursor()
        insert_query = "INSERT INTO resumes (name, email, phone, skills) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (name, user_details['email'], user_details['phone'], ', '.join(user_details['skills'].keys())))
        db.commit()

        return render_template('results.html', name=name, email=user_details['email'], phone=user_details['phone'], skills=', '.join(user_details['skills'].keys()), skills_data=user_details['skills'])
    
    flash('Invalid file format. Please upload a PDF or DOCX file.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
