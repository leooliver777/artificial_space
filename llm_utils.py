# llm_utils.py
from openai import OpenAI
import os
from dotenv import load_dotenv

# ✅ Load the .env file
load_dotenv()

# ✅ Use the environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def label_content_with_ai(text_block):
    prompt = f"""
Label the following PDF content. Use the format:
[TITLE], [HEADING], [PARAGRAPH], [TABLE], [FOOTNOTE], etc.

Content:
{text_block}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            timeout=20,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that labels document content."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] {str(e)}"

def query_pdf_content(user_query, labeled_text):
    prompt = f"""
You are a helpful assistant. Based on the labeled PDF content below, answer the user's question accurately.

Labeled PDF Content:
{labeled_text}

Question:
{user_query}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            timeout=20,
            messages=[
                {"role": "system", "content": "You are an expert at answering questions from document content."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] {str(e)}"
