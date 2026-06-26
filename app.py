import streamlit as st

from resume_parser import read_resume
from agent import analyze_resume_with_ai



st.set_page_config(
    page_title="AI Resume Agent"
)


st.title(
    "🤖 AI Resume Analyzer Agent"
)


st.success(
    "Upload your resume PDF"
)



# PDF Upload

resume_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)



# Job Description

job_description = st.text_area(
    "Paste Job Description"
)



if st.button("Analyze"):


    if resume_file is None:

        st.warning(
            "Please upload a resume PDF"
        )


    elif job_description.strip() == "":

        st.warning(
            "Please add job description"
        )


    else:


        # Extract PDF text

        resume_text = read_resume(
            resume_file
        )



        st.subheader(
            "📄 Extracted Resume Text"
        )


        st.write(
            resume_text[:1000]
        )



        # AI Analysis

        with st.spinner(
            "AI is analyzing..."
        ):


            result = analyze_resume_with_ai(

                resume_text,

                job_description

            )



        st.subheader(
            "🧠 Skills Found"
        )

        st.write(
            result["resume_skills"]
        )



        st.subheader(
            "❌ Missing Skills"
        )

        st.write(
            result["missing_skills"]
        )



        st.subheader(
            "🤖 AI Career Report"
        )

        st.write(
            result["ai_report"]
        )