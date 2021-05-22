import requests
import json


url = "http://127.0.0.1:8000/event/list/"
data = {
    "date_event": "2021-05-20T15:15",
    "group_name": "default",
    "status": "open"}
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Token 0a1e1d633b7d9662a1014bbbf871ab1e5380f93a'}

r = requests.post(url, data=json.dumps(data), headers=headers)
print(r)
