
import ollama
response = ollama.chat(model='gemma:2b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])


#ollama run gemma:2b
