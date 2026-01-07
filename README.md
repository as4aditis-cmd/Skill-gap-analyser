🧠 Skill Gap Analyser – Backend (Pathfinder AI)<br>
This repository contains the backend service for Pathfinder AI, responsible for analyzing a user’s skills against a chosen career and returning missing skills, recommendations, and learning guidance.<br>
The backend is built using Flask and deployed on Render using Gunicorn.<br><br>


🌐 Live API<br>
🔗 Base URL:<br>
https://skill-gap-analyser-ves3.onrender.com<br>
🔗 Health Check:<br>
GET /<br><br>


🛠️ Tech Stack<br>
🐍 Python 3<br>
🌶️ Flask<br>
🔗 Flask-CORS<br>
🚀 Gunicorn (Production server)<br>
☁️ Render (Deployment)<br><br>


📁 Project Structure<br>
skill-gap-analyser/<br>
│<br>
├── app.py               # Main Flask application<br>
├── requirements.txt     # Python dependencies<br>
├── .gitignore<br>
├── README.md<br>
│<br>
├── venv/                # Virtual environment (ignored in git)<br>
├── __pycache__/         # Python cache (ignored in git)<br><br>


🔌 API Endpoints<br>
✅ Health Check<br>
GET /<br>
Response<br>
{<br>
  "status": "Backend is running"<br>
}<br><br>


🎯 Skill Gap Analysis<br>
POST /api/skill-gap<br>

Request Body<br>
{<br>
  "career": "Data Scientist",<br>
  "skills": ["python", "statistics"]<br>
}<br><br>

Response<br>
{<br>
  "career": "Data Scientist",<br>
  "required_skills": [<br>
    "python",<br>
    "statistics",<br>
    "machine learning",<br>
    "sql",<br>
    "data visualization"<br>
  ],<br>
  "known_skills": ["python", "statistics"],<br>
  "missing_skills": [<br>
    "machine learning",<br>
    "sql",<br>
    "data visualization"<br>
  ],<br>
  "completion_percentage": 40<br>
}<br><br>

🧠 Skill Analysis Logic<br>
Career is mapped to a predefined skill set<br>
User-provided skills are normalized<br>
Missing skills are calculated<br>
Completion percentage is computed<br>
JSON response sent to frontend<br>
⚠️ Currently rule-based (no paid AI APIs used), making it free, fast, and hackathon-friendly<br><br>


🔐 CORS Configuration<br>
CORS is enabled to allow frontend access:<br>
from flask_cors import CORS<br>
CORS(app)<br><br>

This allows requests from:<br>
Vercel frontend<br>
Localhost (development)<br><br>


🧪 Run Locally<br>
1️⃣ Clone the repository<br>
git clone https://github.com/as4aditis-cmd/skill-gap-analyser.git<br>
cd skill-gap-analyser<br>
2️⃣ Create virtual environment<br>
python -m venv venv<br>
source venv/bin/activate   # Mac/Linux<br>
venv\Scripts\activate      # Windows<br>
3️⃣ Install dependencies<br>
pip install -r requirements.txt<br>
4️⃣ Run Flask app<br>
python app.py<br><br>


Server will run on:<br>
http://localhost:5000<br><br>


🚀 Production Deployment (Render)<br>
Start Command<br>
gunicorn app:app<br>
Instance Type<br>
Free tier supported<br>
No paid services required<br><br>


📦 requirements.txt<br>
flask<br>
flask-cors<br>
gunicorn<br><br>


🧩 Environment Variables<br>
No required environment variables for MVP.<br>
(Ready for future AI keys if needed)<br><br>


🧠 Future Enhancements<br>
🤖 AI-based skill recommendations (LLM integration)<br>
📚 Learning resource suggestions<br>
🧑‍🎓 Personalized roadmap generation<br>
🔐 Authentication & user-based analysis<br>
📊 Skill proficiency scoring<br><br>


👩‍💻 Author<br>
Aditi Sharma<br>
Backend & Full Stack Developer<br>
GitHub: https://github.com/as4aditis-cmd<br>
Project: Pathfinder AI<br><br>


⭐ Support<br>
If you find this useful:<br>
⭐ Star the repository<br>
🧠 Share feedback<br>
🚀 Fork & build on top of it<br>
🚀 “Identify your gaps. Build your skills. Shape your future.”
