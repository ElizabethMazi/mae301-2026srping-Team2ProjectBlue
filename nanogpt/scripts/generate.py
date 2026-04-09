from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def generate_answer(query, docs):
    context = ""

    for d in docs:
        context += f"\nSource: {d['source']}\nContent: {d['content']}\nImpact: {d['impact']}\n"

    prompt = f"""
You are a local planning assistant for Pima County, Arizona.

Explain clearly how developments affect home buyers.

Question:
{query}

Context:
{context}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
