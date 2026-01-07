TECH_SKILLS = [
    # Programming Languages
    'python', 'java', 'javascript', 'typescript', 'c', 'c++', 'c#', 'go', 'rust', 'php', 'ruby', 'swift', 'kotlin', 'dart', 'scala', 'perl', 'r', 'shell', 'bash',
    # Web Frameworks & Libraries
    'react', 'angular', 'vue', 'nextjs', 'next.js', 'svelte', 'express', 'node.js', 'nodejs', 'flask', 'django', 'fastapi', 'spring boot', 'laravel', 'asp.net', 'jquery', 'bootstrap', 'tailwind', 'redux', 'graphql',
    # Databases
    'sql', 'mysql', 'postgresql', 'postgres', 'mongodb', 'redis', 'sqlite', 'oracle', 'cassandra', 'mariadb', 'dynamodb', 'firebase',
    # Cloud & DevOps
    'aws', 'azure', 'gcp', 'google cloud', 'docker', 'kubernetes', 'jenkins', 'git', 'github', 'gitlab', 'terraform', 'ansible', 'ci/cd', 'nginx', 'linux', 'ubuntu', 'serverless',
    # AI & Data Science
    'machine learning', 'data science', 'deep learning', 'nlp', 'natural language processing', 'computer vision', 'ai', 'artificial intelligence', 'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch', 'keras', 'opencv', 'matplotlib', 'seaborn', 'spark', 'hadoop',
    # Tools & Design
    'figma', 'adobe xd', 'photoshop', 'illustrator', 'ui/ux', 'jira', 'confluence', 'trello', 'slack', 'notion', 'postman',
    # General Soft Skills & Concepts
    'agile', 'scrum', 'project management', 'communication', 'problem solving', 'leadership', 'teamwork', 'analytics', 'tableau', 'power bi', 'excel', 'rest api', 'api design', 'microservices', 'distributed systems', 'testing', 'unit testing', 'frontend', 'backend', 'fullstack'
]

# Curated learning resources for popular skills (Official Docs/Trusted Platforms)
SKILL_RESOURCES = {
    'python': 'https://docs.python.org/3/tutorial/',
    'java': 'https://dev.java/learn/',
    'javascript': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
    'typescript': 'https://www.typescriptlang.org/docs/',
    'react': 'https://react.dev/learn',
    'node.js': 'https://nodejs.org/en/docs/guides/',
    'nodejs': 'https://nodejs.org/en/docs/guides/',
    'flask': 'https://flask.palletsprojects.com/',
    'django': 'https://docs.djangoproject.com/',
    'aws': 'https://aws.amazon.com/getting-started/',
    'docker': 'https://docs.docker.com/get-started/',
    'kubernetes': 'https://kubernetes.io/docs/tutorials/',
    'machine learning': 'https://www.coursera.org/specializations/machine-learning-introduction',
    'data science': 'https://www.kaggle.com/learn',
    'postgresql': 'https://www.postgresql.org/docs/online-resources/',
    'mongodb': 'https://www.mongodb.com/developer/languages/javascript/node-js-quick-start/',
    'git': 'https://git-scm.com/doc',
    'github': 'https://docs.github.com/en/get-started',
    'sql': 'https://www.w3schools.com/sql/',
    'tailwind': 'https://tailwindcss.com/docs',
    'figma': 'https://help.figma.com/hc/en-us/articles/360040328273-Find-resources-for-learning-Figma',
    'fastapi': 'https://fastapi.tiangolo.com/tutorial/',
    'next.js': 'https://nextjs.org/learn',
    'nextjs': 'https://nextjs.org/learn',
    'spring boot': 'https://spring.io/projects/spring-boot',
    'terraform': 'https://developer.hashicorp.com/terraform/tutorials',
}

def refine_skills(extracted_words):
    matched = []
    for word in extracted_words:
        if word.lower() in TECH_SKILLS:
            matched.append(word.lower())
    return list(set(matched))

def analyze_skills(career, user_skills):
    skill_map = {
        "Data Analyst": ["Excel", "SQL", "Python", "Statistics"],
        "Frontend Developer": ["HTML", "CSS", "JavaScript", "React"]
    }

    required = skill_map.get(career, [])
    missing = list(set(required) - set(user_skills))

    return {
        "career": career,
        "missing_skills": missing,
        "level": "Beginner" if len(user_skills) < 2 else "Intermediate"
    }

