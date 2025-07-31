# Local LLM Document QA App

A local web app that lets users upload `.pdf` or `.txt` documents and ask natural language questions. 
The app uses vector similarity to retrieve answers from the uploaded files. If nothing relevant is found, it falls back to a local LLM (via Ollama) for general answers.

# features 
- 📄 Upload `.txt` or `.pdf` files
- 🔍 Ask questions based on uploaded content
- 🤖 Local LLM fallback using Ollama
- ⚡ Fast vector search using FAISS + Sentence Transformers
- 🖥️ Built with FastAPI + Streamlit (or Gradio)
  
# Tech Stack 
- Python
- FastAPI (Backend)
- Streamlit or Gradio (Frontend)
- FAISS + Sentence Transformers (Embeddings + Vector DB)
- PyMuPDF / `open()` (Document Reading)
- Ollama (Local LLM)

#  How It Works
1. User uploads a `.txt` or `.pdf` file
2. File is parsed and converted to text
3. Text is split and embedded using sentence-transformers
4. FAISS index is created and searched based on the user’s query
5. If match found → return answer from doc
6. Else → send query to local LLM via Ollama

# Setup Instructions 

### Clone the repo
git clone https://github.com/HarshithaAchana/ollama-local-llm.git
cd llm-app

### Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

### Run the app
streamlit run app.py
# or
uvicorn main:app --reload

<img width="1340" height="661" alt="image" src="https://github.com/user-attachments/assets/50705575-dada-420f-9b92-59e7fc2665ea" />
Made with ❤️ by Harhitha Achana (https://github.com/HarshithaAchana)
