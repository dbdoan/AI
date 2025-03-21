from dotenv import load_dotenv
from openai import OpenAI
import os

os.system("clear")

load_dotenv()
api_key = os.getenv("OPEN_AI_KEY")


client = OpenAI(
    api_key=api_key
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {
            "role": "user", "content": "how many legs does a cat have?"
        }
    ]
)

print(completion.choices[0].message)