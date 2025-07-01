import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your API key from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt: str, model: str = "gpt-4") -> str:
    """
    Send the prompt to OpenAI and return the assistant's reply.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    # Extract and return the assistant's message
    return response.choices[0].message.content.strip()
