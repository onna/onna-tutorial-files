import json
import requests

base_url = 'https://enterprise.onna.com'
oauth_path = '/auth/oauth/'
user = "stefano@oscillator.es"
container = "stefanoonnanov2020"
account = "stefanoonnanov2020"

resp = requests.get(f'{base_url}/api/{container}/{account}/@oauthgetcode?client_id=canonical&scope={account}')
auth_code = resp.json()['auth_code']
print(f"auth_code: {auth_code}")
