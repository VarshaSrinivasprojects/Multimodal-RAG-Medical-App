# Multimodal RAG System for Medical Applications

## A FastAPI + Gradio app for medical decision support using multimodal Retrieval-Augmented Generation (RAG). Combines clinical notes and AI-powered insights to assist diagnosis and treatment planning. 

##Key Features:

💡 Retrieval-Augmented Generation using Bio/Clinical domain LLMs

📄 Ingests and understands structured/unstructured medical notes

🧠 FastAPI-powered backend with a user-friendly Gradio interface

🔍 Future support for X-ray and radiology image interpretation

## Technologies
- Python
- FastAPI
- Gradio
- Hugging Face Transformers

## How to Run
```bash
# Clone the repo
git clone https://github.com/your-username/multimodal-rag-medical-app.git
cd multimodal-rag-medical-app

# Install dependencies
pip install -r requirements.txt

# Run FastAPI backend
uvicorn app.main:app --reload

# Run Gradio UI
python gradio_ui/interface.py
```

## Features
- Upload medical notes (text)
- Upload diagnostic images (coming soon)
- Embeds and retrieves relevant data
- Generates medical insights using LLM

## Future Improvements
- Add multimodal LLMs like LLaVA or BioMedGPT
- Expand dataset and fine-tune with domain-specific knowledge
