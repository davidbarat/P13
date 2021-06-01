import requests
import json


url = 'http://127.0.0.1:8000/event/list/'
data = {
    "date_event": "2021-06-01T15:15:11",
    "group_name": "Sarkozy",
    "status": "open"}
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Token bda31a987eae0d08a943a062d477fbc5b7c3bf97'}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r)
