
# AI-Powered Resume Analyzer

## Overview

The **AI-Powered Resume Analyzer** is a web application that allows users to upload their resumes, extract relevant skills and personal details, and store them in a MySQL database. This application is built using Flask for the backend, HTML/CSS for the frontend, and utilizes basic text extraction techniques to analyze resumes.

## Features

- Upload resumes in plain text or PDF format.
- Extract and display user details: Name, Email, Phone Number.
- Extract skills and calculate relevance scores.
- Save extracted details to a MySQL database.
- User-friendly interface with a responsive design.

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Flask
- **Database**: MySQL
- **Libraries**: 
  - `Flask` for web framework
  - `mysql-connector-python` for MySQL connection
  - `PyPDF2` for PDF parsing
  - `python-docx` for .docx file parsing

## Getting Started

### Prerequisites

- Python 3.x
- MySQL server installed
- Basic knowledge of Flask and web development

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Piyush-Kumar11/ai-powered-resume-analyzer.git
   cd ai-powered-resume-analyzer
   ```

### Running the Application

1. **Start the Flask application**:
   ```bash
   FLASK_APP=app.py flask run
   ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000` to access the application.

### Usage

1. On the home page, enter your name, upload your resume, and click "Submit."
2. The application will extract the relevant information from the uploaded resume.
3. The results page will display your name, email, phone number, and extracted skills, along with their relevance scores.
4. The extracted data will be saved in the MySQL database.

## Error Handling

The application includes basic error handling for:
- Invalid file uploads
- Database connection issues
- Empty inputs

## Deployment

For deploying this application on AWS, follow these steps:

1. Create an AWS account and launch an EC2 instance.
2. Install the required software on your EC2 instance (Python, Flask, etc.).
3. Upload your application code to the instance.
4. Configure your web server (optional) for production use.

### Notes

- Ensure to secure your AWS resources and monitor usage to stay within the Free Tier limits.
- For any issues or contributions, feel free to raise an issue or submit a pull request.

## Author

**Piyush Kumar**  
- [GitHub](https://github.com/Piyush-Kumar11)
- [LinkedIn](https://linkedin.com/in/piyush2tiger/)

## License

This project is licensed under the MIT License.  
**Author:** Piyush Kumar  
See the [LICENSE](LICENSE) file for details.
