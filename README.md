# Midas

# Prerequisites
Most software is available via standard package managers or direct downloads:

- Python 3.8 or higher | https://www.python.org/downloads/
- Ollama for installing and running local LLM models | https://ollama.com/download
- An installed LLM model in Ollama (e.g., llama3.1) | `ollama pull llama3.1`
- Just command runner | https://github.com/casey/just

To run:
1. Create a virtual environment: `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python prompt.py`