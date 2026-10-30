from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads OPENAI_API_KEY from .env
client = OpenAI()

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful teaching assistant."},
            {"role": "user", "content": "Respond with exactly the word: 'Success!'"},
        ],
        temperature=0.0,
    )
    print(f"Setup complete. Model response: {response.choices[0].message.content}")
    print(f"Tokens used: {response.usage.total_tokens}")
except Exception as e:
    print(f"Setup failed: {e}")