import requests

resp = requests.get('http://server:8004/test')
print(resp.text)

resp = requests.post('http://server:8004/test')
print(resp.text)
