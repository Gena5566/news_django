import requests
import pprint


#response = requests.get("http://127.0.0.1:8000/api/v0/posts/", auth=('___', '_____))

#pprint.pprint(response.json())

token = 'e5cc6bc3bb937ff384c98d5f3ee92e266e0ff9e8'
headers = {'Authorization': f'Token {token}'}
response = requests.get("http://127.0.0.1:8000/api/v0/posts/", headers=headers)

pprint.pprint(response.json())