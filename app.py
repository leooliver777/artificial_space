# app.py
import gradio as gr
from pdf_utils import extract_pdf_content
from llm_utils import label_content_with_ai, query_pdf_content

labeled_text_global = ""

def process_pdf(file):
    global labeled_text_global
    try:
        print(f"[INFO] File received: {file.name}")
        content = extract_pdf_content(file.name)
        print(f"[INFO] Extracted {len(content)} pages")

        labeled = []
        for c in content:
            print(f"[INFO] Labeling Page {c['page']}...")
            result = label_content_with_ai(c['text'])
            labeled.append(f"Page {c['page']}\n{result}")
            print(f"[INFO] Done with Page {c['page']}")

        labeled_text_global = "\n\n".join(labeled)
        return labeled_text_global

    except Exception as e:
        print(f"[ERROR] in process_pdf: {str(e)}")
        return f"[ERROR] {str(e)}"



def handle_query(query):
    try:
        return query_pdf_content(query, labeled_text_global)
    except Exception as e:
        print(f"[ERROR] handle_query failed: {str(e)}")
        return f"[ERROR] Failed to process query: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("## PDF Content Labeling and Query Tool")
    with gr.Row():
        file_input = gr.File(label="Upload PDF")
        output_text = gr.Textbox(label="Labeled Content", lines=20)
    with gr.Row():
        query_input = gr.Textbox(label="Ask a Question")
        query_output = gr.Textbox(label="Answer")

    file_input.change(process_pdf, inputs=file_input, outputs=output_text)
    query_input.change(handle_query, inputs=query_input, outputs=query_output)

demo.launch(share=True)
