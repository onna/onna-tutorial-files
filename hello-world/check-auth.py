#!.venv/bin/python
# The above python interpreter is set to a venv, located in .venv of this directory.
# If you use another venv this needs to be adjusted!
import json
import requests

base_url = 'https://enterprise.onna.com'
oauth_path = '/auth/oauth/'
user = "you@onna.com"
container = "container"
account = "account"

resp = requests.get(f'{base_url}/api/{container}/{account}/@oauthgetcode?client_id=canonical&scope={account}')
auth_code = resp.json()['auth_code']
print(f"auth_code: {auth_code}")
