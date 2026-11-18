pip install openai

from openai import OpenAI

client = OpenAI()

prompt = input("Enter a prompt: ")

response = client.responses.create(
    model="gpt-3.5-turbo-instruct",
    input=prompt
)

print("Generated Text:")
print(response.output_text)
