import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

api_key=""

url = input("Paste the url\n")

headers = {'API-Key': os.getenv("url_scan_api_key"),'Content-Type':'application/json'}
data = {"url": f'{url}', "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())