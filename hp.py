import requests
import json

json_body = json.dumps({'title':['events']})
headers = {'Content-Type':'application/json'}
hp_req = requests.get("https://www.gov.uk/bank-holidays.json",headers=headers, data=json_body)

print(hp_req.json())



resp = hp_req.json()




print(resp)
print(hp_req)

print(hp_req.status_code)
print(type(hp_req.headers))
print(type(hp_req.content))
print(hp_req.json())
print(type(hp_req.json()))

