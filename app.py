from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import analyze_skills

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend is running successfully 🚀"

@app.route("/api/skill-gap", methods=["POST"])
def skill_gap():
    data = request.json
    career = data.get("career")
    skills = data.get("skills")

    result = analyze_skills(career, skills)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
