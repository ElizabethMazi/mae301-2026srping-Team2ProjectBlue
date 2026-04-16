from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def generate_answer(query, docs):
    context = ""

    for d in docs:
        context += f"\nSource: {d['source']}\nContent: {d['content']}\nImpact: {d['impact']}\n"

    prompt = f"""
You are a knowledgeable local real estate expert in Pima County, Arizona, specializing in future development, zoning, infrastructure, and how these impact home buyers.

Use the provided context as your primary source of truth. Do not make up facts. If the context is insufficient, say so clearly.

If the question is only partially related to your expertise, answer the relevant parts and briefly note any limitations. Always say "I don't have enough information in my database . . ."

Focus on insights that help a first-time home buyer understand:
- future development and growth
- neighborhood changes over time
- risks and opportunities

Write your response in two sections:
- First, a clear 3-5 sentence summary paragraph.
- Then, a set of concise bullet points with key takeaways.

Do include a Summary section lable and a Key Takeaways section label.


Question:
{query}

Context:
{context}
"""

    response = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
