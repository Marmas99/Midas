setup:
    #!/usr/bin/env bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

run: setup
    #!/usr/bin/env bash
    source venv/bin/activate
    python3 prompt.py