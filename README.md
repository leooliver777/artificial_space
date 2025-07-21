# 📄 PDF Content Labeling and Query Interface

This project is a simple AI-powered web application that allows users to upload PDF documents and ask questions about their content. It extracts text from the uploaded PDF and uses a question-answering model to return relevant answers.

## 🚀 Features

- Upload any PDF file through a Gradio interface
- Extract and preprocess text using `PyMuPDF`
- Ask natural language questions about the content
- Get relevant answers using Hugging Face's Transformers
- Simple and clean UI built with Gradio

## 🛠 Tech Stack

- **Python 3.9+**
- **Gradio** – UI interface
- **PyMuPDF (fitz)** – PDF text extraction
- **Transformers (Hugging Face)** – Question Answering (QA) pipeline
- **Pretrained Model** – `distilbert-base-cased-distilled-squad`

## 📂 Project Structure

pdf-qa-app/
├── app.py                  # Main application script
├── sample_pdfs/            # Sample PDFs for testing
│   ├── AI_Intro.pdf
│   └── Rainforest_Ecosystem.pdf (etc.)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation

## 💡 How It Works

1. User uploads a PDF file.
2. The backend extracts plain text using `fitz`.
3. The user enters a natural language question.
4. The `transformers` QA model searches the text for the best answer.
5. The result is displayed on the screen.

## 🖥️ Run Locally

1. **Clone this repo**

```bash
git clone https://github.com/yourusername/pdf-qa-app.git
cd pdf-qa-app
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
python app.py
```

The app will open in your browser at `http://127.0.0.1:7860`.

## 📦 requirements.txt

gradio==3.50.2
transformers
torch
PyMuPDF

## 🧠 Model Info

Default model used:  
`distilbert-base-cased-distilled-squad`  
(A lightweight, pretrained question-answering model fine-tuned on the SQuAD dataset.)

## 📁 Sample PDFs

Use the included PDFs like:
- AI_Intro.pdf
- Rainforest_Ecosystem.pdf
- Water_Cycle.pdf

These help in testing the model’s ability to extract and answer questions correctly.

## 🔧 Notes

- If the model returns irrelevant answers, ensure the PDF has readable text and not scanned images.
- For large PDFs, answers may degrade in accuracy. Limit file size or segment text accordingly.
- Upgrade Gradio or use GPU for better performance.

## 📜 License

MIT License
