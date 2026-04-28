from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def prepare_text(row):
    return f"Content: {row['content']} Impact: {row['impact']}"

def embed(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding
