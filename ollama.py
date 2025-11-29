import requests
import json

# URL for the local Ollama server
OLLAMA_URL = "http://localhost:11434/api/generate"

# The prompt you want to send
prompt = "Hello"

# Build the request payload
payload = {
    "model": "llama3.1",   # name of your installed model
    "prompt": prompt
}

# Send the request
response = requests.post(OLLAMA_URL, json=payload, stream=True)

# The API streams chunks, so read them line by line
for line in response.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        print(data.get("response", ""), end="", flush=True)

print()  # newline at the end