import gradio as gr
import requests

def ask_backend(context, question):
    response = requests.post(
        "http://localhost:8000/ask",
        data={"context": context, "question": question}
    )
    return response.json().get("answer", "Error")

iface = gr.Interface(
    fn=ask_backend,
    inputs=["text", "text"],
    outputs="text",
    title="Medical RAG Assistant",
    description="Ask questions about medical records and get answers using an LLM"
)

iface.launch()
