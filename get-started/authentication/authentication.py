import json
import requests

base_url = 'https://enterprise.onna.com'
oauth_path = '/auth/oauth/'
user = "USERNAME"
container = "CONTAINER"
account = "ACCOUNT"
password = "PASSWORD"

resp = requests.get(f'{base_url}/api/{container}/{account}/@oauthgetcode?client_id=canonical&scope={account}')
auth_code = resp.json()['auth_code']
print(f"auth_code: {auth_code}")

payload = {'grant_type': "user",
           'code': auth_code,
           'username': user,
           'password': password,
           'scopes': account,
           'client_id': "canonical"
          }
headers = {'Accept': 'application/json'}
resp = requests.post(f'{base_url}/{oauth_path}/get_auth_token', headers=headers, data=json.dumps(payload))
jwt_token = resp.text
print(f"jwt_token: {jwt_token}")

headers = {'Accept': 'application/json', 'Authorization': "Bearer {}".format(jwt_token)}
resp = requests.post(f'{base_url}/{oauth_path}/me', headers=headers)
print(f"Account info: {resp.json()}")

resp = requests.get(f"{base_url}/api/{container}/{account}/{user}", headers=headers)
print(f"{user}: {resp.json()}")

resp = requests.get(
    f"{base_url}/api/{container}/{account}/@statusAccount", headers=headers
)
print(f"Account status: {resp.json()}")
