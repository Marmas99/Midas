import requests
import json

# URL for the local Ollama server
OLLAMA_URL = "http://localhost:11434/api/generate"


print("Welcome")
print("Type 'exit' or 'quit' to end the session.")
print("------------------------------------------")

while True:
    prompt = input(">>> ")
    if prompt.lower() in ["exit", "quit"]:
        break

    payload = {
        "model": "llama3.1",   # name of your installed model
        "prompt": prompt
    }
    
    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            print(data.get("response", ""), end="", flush=True)

    print()