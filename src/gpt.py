import json
import requests
import os
from dotenv import load_dotenv


load_dotenv()

def get_gpt_res(prompt):
    URL = "https://api.openai.com/v1/chat/completions"
    OPENAI_KEY = os.getenv('GPT_API_KEY')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages" : [{"role": "user","content": f"{prompt}"}]
    }
    response = requests.post(URL, data=json.dumps(payload), headers=headers)
    return response.json()['choices'][0]['message']['content']