# Multimodal RAG System for Medical Applications

A prototype application that combines patient notes and medical images to assist with healthcare decisions using Retrieval-Augmented Generation (RAG).

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
