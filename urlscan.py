import requests
import json
from dotenv import load_dotenv
import os
#Python script to run urls through urlscan.io

load_dotenv()

api_key="" #api key pulled from environment

url = input("Paste the url\n")

headers = {'API-Key': os.getenv("your_api_key"),'Content-Type':'application/json'} #header for pulling api key from environment
data = {"url": f'{url}', "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json())
