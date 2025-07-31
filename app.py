# app.py
import gradio as gr
from document_handler import extract_text_from_file
from vector_store import VectorStore
from llm_helper import ask_ollama

vector_store = VectorStore()

def handle_user_input(user_input, files):
    if files:
        full_text = ""
        for file in files:
            full_text += extract_text_from_file(file.name) + "\n"
        vector_store.add_document(full_text)

        # Search document for answer
        results = vector_store.search(user_input, top_k=1)
        if results and results[0].strip():
            return f"📄 **Answer from Document**:\n\n{results[0]}"
    
    # Fallback to LLM
    response = ask_ollama(user_input)
    return f"💡 **Answer from Ollama**:\n\n{response}"

with gr.Blocks() as demo:
    gr.Markdown("# 📚 Local LLM Assistant")
    gr.Markdown("Upload a `.pdf` / `.txt` or ask a question directly.")

    with gr.Row():
        file_input = gr.File(file_types=[".pdf", ".txt"], file_count="multiple", label="Upload Document(s)")

    user_input = gr.Textbox(lines=2, placeholder="Ask your question here...", label="Your Question")
    output = gr.Textbox(label="Answer")

    submit_btn = gr.Button("Submit")
    submit_btn.click(fn=handle_user_input, inputs=[user_input, file_input], outputs=output)

demo.launch()
