from openai import OpenAI
import os

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named zara, skilled in general task like alexa and google cloud"},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message.content)