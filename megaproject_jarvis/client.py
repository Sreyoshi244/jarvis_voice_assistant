from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(
    api_key="yourkey"
    )

# Make a chat completion request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named Jarvis."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the assistant's reply
print(response.choices[0].message.content)