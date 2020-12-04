headers = {'Accept': 'application/json', 'Authorization': "Bearer {}".format(jwt_token)}
resp = requests.post(f'{base_url}/{oauth_path}/me', headers=headers)
print(resp.json())
