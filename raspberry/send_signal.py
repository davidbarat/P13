import requests
import json
from datetime import datetime


group_name = "Sarkozy"
now = datetime.now()
dt_formated = now.strftime("%Y-%m-%dT%H:%M:%S")
status = "open"

url = 'http://127.0.0.1:8000/event/list/'
data = {
    "date_event": dt_formated,
    "group_name": group_name,
    "status": status}
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Token bda31a987eae0d08a943a062d477fbc5b7c3bf97'}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r)
