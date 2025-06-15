import streamlit as st
import os
import pandas as pd
from resume_utils import extract_text_from_pdf, rank_resumes

# Streamlit UI
st.set_page_config(page_title="AI Resume Ranker", page_icon="🧠")
st.title("🧠 AI Resume Ranker")
st.write("Upload resumes and a job description to rank them based on relevance.")

uploaded_resumes = st.file_uploader("Upload Resumes (PDF only)", type="pdf", accept_multiple_files=True)
job_description = st.text_area("Paste Job Description Here")

if st.button("Rank Resumes"):
    if uploaded_resumes and job_description:
        with st.spinner("Processing resumes..."):
            resumes = {}
            for uploaded_file in uploaded_resumes:
                text = extract_text_from_pdf(uploaded_file)
                resumes[uploaded_file.name] = text

            result_df = rank_resumes(resumes, job_description)
            st.success("Ranking complete! 🎉")
            st.dataframe(result_df)

            # Download option
            csv = result_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Results", csv, "Score_Output.csv", "text/csv")
    else:
        st.warning("⚠️ Please upload resumes and provide a job description.")
