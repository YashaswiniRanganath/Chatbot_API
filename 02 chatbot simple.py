import openai
from apikey import API_KEY

openai.api_key = API_KEY

output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "write me a script for hosting a conference on technology"}]
)

print(output)


