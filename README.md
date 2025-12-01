# Midas

# Prerequisites
## Software
Most software is available via standard package managers or direct downloads:

- Python 3.8 or higher | https://www.python.org/downloads/
- Ollama for installing and running local LLM models | https://ollama.com/download
- An installed LLM model in Ollama (e.g., llama3.1) | `ollama pull llama3.1`
- Just command runner | https://github.com/casey/just

## Setup Instructions
1. Run `Ollama serve ` to start the local Ollama server and keep it running
2. If its your first time running, run `Ollama pull llama3.1` to download the model, you can choose any model you like
3. Run `just run` to start the prompt interface