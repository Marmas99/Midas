import requests
import json

# URL for the local Ollama server
OLLAMA_URL = "http://localhost:11434/api/generate"

# The prompt you want to send
prompt = "Are you offline right now?, What i mean is im running this on my local machine, so are you able to access the internet? And when you answer do you use your own local data or do you access the internet to answer my questions?"

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