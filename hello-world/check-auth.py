#!.venv/bin/python
# The above python interpreter is set to a venv, located in .venv of this directory.
# If you use another venv this needs to be adjusted!
import json
import requests

# Configuration Variables like username, account name, etc
base_url = "https://enterprise.onna.com"
oauth_path = "/auth/oauth/"
user = "you@onna.com"
container = "container"
account = "account"

# GET request using the API to get your auth code and print it in the terminal.
resp = requests.get(
    f"{base_url}/api/{container}/{account}/@oauthgetcode?client_id=canonical&scope={account}"
)
auth_code = resp.json()["auth_code"]
print(f"auth_code: {auth_code}")
