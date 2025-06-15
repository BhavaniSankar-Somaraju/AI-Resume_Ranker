import fitz  # PyMuPDF
import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def rank_resumes(resume_texts: dict, job_description: str) -> pd.DataFrame:
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    data = []

    for name, text in resume_texts.items():
        resume_embedding = model.encode(text, convert_to_tensor=True)
        score = util.cos_sim(job_embedding, resume_embedding).item()
        data.append({"Resume Name": name, "Similarity Score": round(score, 3)})

    return pd.DataFrame(data).sort_values(by="Similarity Score", ascending=False)
