# 🧠 AI Resume Ranker 🔍

This project is an AI-powered tool that **automatically ranks resumes** based on their **relevance to a given job description** using Natural Language Processing (NLP) and semantic similarity techniques.

## 🚀 Features

- 📄 Extracts text from multiple PDF resumes
- 📌 Compares resumes against a job description using **Sentence Transformers**
- 📊 Outputs a CSV file (`Score_Output.csv`) with similarity scores
- ✅ Ideal for recruiters, HR teams, and automated hiring pipelines

---

## 🛠️ Tech Stack

- Python 🐍
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) – PDF Text Extraction
- [Sentence Transformers](https://www.sbert.net/) – Semantic similarity via `all-MiniLM-L6-v2`
- Pandas – Data handling and scoring

---

## 📁 Project Structure

```
ai-resume-ranker/
├── resume_ranker.ipynb          # Jupyter notebook with all logic
├── Sample_Resumes/              # Folder with input PDF resumes
│   ├── Resume1.pdf
│   └── Resume2.pdf
├── Job_Description.txt          # Text file containing job description
├── Score_Output.csv             # Output: resume scores
├── README.md                    # Project documentation
└── requirements.txt             # Dependencies
```

---

## 📌 How It Works

1. You place resumes in the `Sample_Resumes/` folder.
2. Add your job description inside `Job_Description.txt`.
3. Run the notebook `resume_ranker.ipynb`.
4. The model compares resumes and outputs a ranked list in `Score_Output.csv`.

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/BhavaniSankar-Somaraju/Ai_Resume_Ranker.git
cd Ai_Resume_Ranker

# Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Sample Output

| Resume Name | Similarity Score |
|-------------|------------------|
| Resume1.pdf | 0.874            |
| Resume2.pdf | 0.652            |

---

## 💡 Future Improvements

- Add a **Streamlit Web UI** for file upload + real-time scoring
- Support for **DOCX** and plain text resumes
- Integration with **ATS (Applicant Tracking System)** tools
- Add a **visual dashboard** for result analytics

---

## 👨‍💻 Author

**Bhavani Sankar Somaraju**  
📫 [LinkedIn](https://www.linkedin.com/in/bhavanisankar-somaraju) | [GitHub](https://github.com/BhavaniSankar-Somaraju)

---

## 📜 License

This project is licensed under the MIT License.
