import os
import json

from dotenv import load_dotenv
import google.generativeai as genai


# Load .env
load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")


if not API_KEY:
    raise Exception(
        "GEMINI_API_KEY not found. Check .env file"
    )


# Configure Gemini

genai.configure(
    api_key=API_KEY
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# =====================
# Gemini AI Function
# =====================

def ask_ai(prompt):

    response =model.generate_content(prompt)

    return response.text



# =====================
# Load Skills
# =====================

def load_skills():

    with open(
        "skills.json",
        "r"
    ) as file:

        return json.load(file)



# =====================
# Extract Skills
# =====================

def extract_skills(text):

    skills = load_skills()

    found = []

    text = text.lower()


    for skill in skills:

        if skill.lower() in text:

            found.append(skill)


    return list(set(found))



# =====================
# AI Resume Analyzer
# =====================

def analyze_resume_with_ai(
    resume_text,
    job_description
):


    resume_skills = extract_skills(
        resume_text
    )


    job_skills = extract_skills(
        job_description
    )



    missing_skills = list(
        set(job_skills)
        -
        set(resume_skills)
    )



    prompt = f"""

You are an AI Resume Analyzer Agent.


Resume:

{resume_text}


Job Description:

{job_description}


Detected Resume Skills:

{resume_skills}


Missing Skills:

{missing_skills}


Generate:

1. Resume analysis

2. Skill gaps

3. Improvement suggestions

4. AI/ML projects to add

5. Suitable job roles


"""


    response = ask_ai(
        prompt
    )



    return {


        "resume_skills": resume_skills,


        "job_skills": job_skills,


        "missing_skills": missing_skills,


        "ai_report": response

    }