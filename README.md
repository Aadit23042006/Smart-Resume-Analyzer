# 🤖 AI Resume Analyzer Agent

A **Streamlit** application that analyzes a resume against a job description using a skill-keyword matcher plus **Google Gemini** for AI-generated career feedback — including skill gaps, improvement suggestions, project ideas, and suitable job roles.

---

## ✨ Features

- **PDF resume upload & text extraction** via `pypdf`.
- **Skill extraction** — scans resume and job description text against a curated list of skills (`skills.json`) to detect matches.
- **Gap analysis** — automatically computes which skills appear in the job description but are missing from the resume.
- **AI-generated career report** via Gemini (`gemini-2.5-flash`), covering:
  1. Resume analysis
  2. Skill gaps
  3. Improvement suggestions
  4. Suggested AI/ML projects to add
  5. Suitable job roles
- **Semantic resume–job matching** (`matcher.py`) using `sentence-transformers` embeddings and cosine similarity for a similarity score.
- **RAG-ready vector indexing** (`rag.py`) that chunks text and builds a FAISS index of resume content for future retrieval-augmented features.

---

## 🗂️ Project Structure

```
ai_resume_agent/
├── app.py                 # Streamlit UI: upload resume, paste job description, run analysis
├── agent.py                 # Gemini integration + skill extraction + AI report generation
├── resume_parser.py          # PDF text extraction (pypdf)
├── matcher.py                 # Semantic similarity scoring (sentence-transformers + cosine similarity)
├── rag.py                      # Text chunking + FAISS vector index builder
├── skills.json                  # Master list of recognized technical skills
├── requirements.txt              # Python dependencies
└── .env                            # API key configuration (not committed)
```

---

## ⚙️ Requirements

- Python 3.9+
- A **Google Gemini API key**

Dependencies (see `requirements.txt`):

```
streamlit
pypdf
langchain
langchain-community
sentence-transformers
faiss-cpu
google-generativeai
scikit-learn
```

---

## 🔧 Setup

1. **Navigate into the project folder:**
   ```bash
   cd ai_resume_agent
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables.** Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then, in the browser window:

1. **Upload your resume** as a PDF.
2. **Paste the target job description** into the text area.
3. Click **Analyze**.

The app will display:
- The extracted resume text (first 1000 characters)
- Skills found in your resume
- Skills required by the job description that are missing from your resume
- A full AI-generated career report (analysis, gaps, suggestions, project ideas, and suitable roles)

---

## 🧠 How It Works

1. **`resume_parser.read_resume()`** extracts raw text from the uploaded PDF.
2. **`agent.extract_skills()`** performs a case-insensitive substring match against the skills list in `skills.json`, applied separately to the resume text and job description.
3. **`agent.analyze_resume_with_ai()`**:
   - Computes `missing_skills` = job skills − resume skills.
   - Builds a structured prompt containing the resume, job description, detected skills, and missing skills.
   - Sends the prompt to Gemini (`gemini-2.5-flash`) and returns the generated report alongside the skill data.
4. **`matcher.match_resume_job()`** (available for use, not yet wired into `app.py`) encodes the resume and job description with a `sentence-transformers` model (`all-MiniLM-L6-v2`) and returns a 0–100 cosine-similarity match score.
5. **`rag.create_vector_database()`** (available for use, not yet wired into `app.py`) splits text into 500-character chunks, embeds them, and builds a FAISS `IndexFlatL2` for future semantic search / RAG functionality.

---

## 🛠️ Tech Stack

| Component            | Technology                              |
|------------------------|------------------------------------------|
| UI                     | Streamlit                                |
| LLM                    | Google Gemini (`gemini-2.5-flash`)        |
| PDF parsing            | pypdf                                     |
| Embeddings             | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector search           | FAISS                                      |
| Similarity scoring       | scikit-learn (cosine similarity)             |

---

## ⚠️ Limitations & Notes

- Skill detection is a **keyword/substring match** against `skills.json`, not a semantic understanding of skill equivalence — customize `skills.json` to expand coverage.
- `matcher.py` and `rag.py` provide additional matching/RAG capabilities that are implemented but **not yet integrated** into the main `app.py` flow — they can be wired in for a match-score display or deeper Q&A over the resume.
- No persistence — analysis results are not saved between sessions.

---

## 📄 License

This project is provided as-is for educational and personal use. Add a license of your choice before distributing.
