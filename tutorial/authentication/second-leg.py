payload = {'grant_type': "user",
           'code': auth_code,
           'username': "stefano@oscillator.es",
           'password': 'iLuFJuYSGYQ58r3*',
           'scopes': [f"{account}"],
           'client_id': "canonical"
          }
headers = {'Accept': 'application/json'}
resp = requests.post(f'{base_url}/{oauth_path}/get_auth_token', headers=headers, data=json.dumps(payload))
jwt_token = resp.text
print(f"jwt_token: {jwt_token}")
