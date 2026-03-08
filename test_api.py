import json
import os

import requests
from dotenv import load_dotenv

# Load the key
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
MODEL = "claude-sonnet-4-6"

# Basic check
if not api_key:
    print("ANTHROPIC_API_KEY not set")
    exit(1)

# Define the host
url = "https://api.anthropic.com/v1/messages"

# Authenticate
headers = {
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

# Construct the payload
payload = {
    "model": MODEL,
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": "Hello, are you ready to code?"
        }
    ]
}

# Run
print("Sending request to Claude")
response = requests.post(url, headers=headers, json=payload, timeout=120)

# Inspect raw result
print(f"Status: {response.status_code}")

if response.status_code == 200:
    # Success
    print("Response:")
    print(json.dumps(response.json(), indent=2))
else:
    # Failure
    print(f"Error: {response.status_code}")
    print("Error:", response.text)
