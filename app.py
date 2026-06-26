import streamlit as st

from agent import analyze_resume_with_ai


st.set_page_config(
    page_title="AI Resume Agent",
    layout="wide"
)


st.title("🤖 AI Resume Agent")


st.success("App is running successfully ✅")


resume_text = st.text_area(
    "Paste your resume",
    height=250
)


job_description = st.text_area(
    "Paste Job Description",
    height=200
)



if st.button("Analyze"):


    if resume_text.strip() == "":

        st.warning("Please paste your resume")


    elif job_description.strip() == "":

        st.warning("Please paste job description")


    else:


        result = analyze_resume_with_ai(
            resume_text,
            job_description
        )


        st.subheader("🤖 AI Career Report")


        st.write(
            result["ai_report"]
        )