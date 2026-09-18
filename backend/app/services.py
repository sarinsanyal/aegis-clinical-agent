import os
from groq import Groq

def analyze_clinical_notes(notes: str) -> str:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    prompt = f"""
    You are an expert clinical AI assistant. Summarize the following patient medical notes.
    Extract key diagnostic details, medications, and risk factors into a concise bulleted list:
    
    {notes}
    """
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-120B",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=500
    )
    
    return response.choices[0].message.content