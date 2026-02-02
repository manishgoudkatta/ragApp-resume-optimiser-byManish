import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEBIUS_API_KEY")

url = "https://api.studio.nebius.ai/v1/models"
headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)
print(response.json())  # this will print all models your key can access
