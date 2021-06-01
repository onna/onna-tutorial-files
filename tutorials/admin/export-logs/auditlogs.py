import argparse
import json
import sys
import requests


from dateutil.parser import parse


argparser = argparse.ArgumentParser(
    description="Download Onna audit logs",
    epilog="Write to a file in the /tmp directory",
)
argparser.add_argument(
    "--username",
    required=True,
    type=str,
    help="Service Account username",
)
argparser.add_argument(
    "--password",
    required=True,
    type=str,
    help="Account password",
    )
argparser.add_argument(
    "--account",
    required=True,
    type=str,
    help="The name of your Onna account",
)
argparser.add_argument(
    "--account_url",
    required=True,
    type=str,
    help="The URL of your account, e.g https://ACMECORP.onna.io or https://enterprise.onna.com",
)
argparser.add_argument(
    "--from_date",
    required=True,
    type=str,
    help="Start date. Most date formats are accepted",
)
argparser.add_argument(
    "--to_date",
    required=True,
    type=str,
    help="End date. Most date formats are accepted",
)
argparser.add_argument(
    "--fname",
    required=True,
    type=str, help="Set filename to save file as",
    )
argparser.add_argument(
    "--container",
    required=False,
    default="rel0",
    help="Name of the account container",
)
argparser.add_argument(
    "--size",
    required=True,
    default="10",
    type=str,
    help="Result size",
)


def auth_code(url=None):
    if not url:
        raise Exception
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()["auth_code"]


def auth_token(auth_code, username, password, scope, base_url):
    payload = {
        "grant_type": "user",
        "code": auth_code,
        "username": username,
        "password": password,
        "scopes": [scope],
        "client_id": "canonical",
    }
    headers = {"Accept": "application/json"}
    resp = requests.post(
        f"{base_url}/auth/oauth/get_auth_token",
        headers=headers,
        data=json.dumps(payload),
    )
    if resp.status_code == 200:
        jwt_token = resp.text
    return jwt_token


def activity_log(
    dt_from, dt_to, size, jwt_token, base_url, account, container, cursor=None
):
    headers = {"Accept": "application/json", "Authorization": f"Bearer {jwt_token}"}
    url = f"{base_url}/api/{container}/{account}/@activityLog?epoch_from={dt_from}&epoch_to={dt_to}&size={size}"
    if cursor is not None:
        url = f"{base_url}/api/{container}/{account}/@activityLog?epoch_from={dt_from}&epoch_to={dt_to}&size={size}&cursor={cursor}"

    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp


def write_log(fname, resp):
    fname = f"/tmp/{fname}.json"
    # write the file to /tmp/
    with open(fname, "w") as f:
        for chunk in resp:
            json.dump(chunk, f)


def main():
    try:
        from_date = int(parse(args.from_date).timestamp())
    except (TypeError, ValueError):
        sys.exit(1)
    try:
        to_date = int(parse(args.to_date).timestamp())
    except (TypeError, ValueError):
        sys.exit(1)

    username = args.username
    password = args.password
    account = args.account
    base_url = args.account_url
    container = args.container
    fname = args.fname
    size = args.size

    auth_code_url = f"{base_url}/api/{container}/{account}/@oauthgetcode?client_id=canonical&scope={account}"
    code = auth_code(auth_code_url)
    token = auth_token(code, username, password, account, base_url)

    result = activity_log(from_date, to_date, size, token, base_url, account, container)
    cursor = result.json().get("cursor", None)
    user_activity_response = list()
    user_activity_response = result.json()["items"]
    if cursor is not None:
        while cursor is not None:
            result = activity_log(
                from_date, to_date, size, token, base_url, account, container, cursor
            )
            user_activity_response.append(result.json())
            cursor = result.json().get("cursor", None)

    fname = f"{fname}_user_activity_{from_date}-{to_date}"
    write_log(fname, user_activity_response)


if __name__ == "__main__":
    args = argparser.parse_args()
    main()

