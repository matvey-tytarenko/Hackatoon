from openai import OpenAI
import os

GPT4o="gpt-4o"
GPT4omini="gpt-4o-mini"
OPEN_API_KEY=""

client = OpenAI(api_key=OPEN_API_KEY)

completion = client.chat.completions.create(
  model=GPT4o,
  messages=[
    {"role": "user", "content": "Tell me about programming in 2 sentences."}
  ]
)

print(completion.json())
