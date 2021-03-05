# -*- encoding: utf-8 -*-
import argparse
import csv
import json
import requests
import sys

from dateutil.parser import parse


argparser = argparse.ArgumentParser(
    description="Create a Preservation in a workspace from Slack Enterprise Datasource",
    epilog="You can also get a list of existing Slack Enterprise Datasources in your account",
)
argparser.add_argument(
    "--username", required=True, type=str, help="Onna Account username"
)
argparser.add_argument("--password", required=True, type=str, help="password")
argparser.add_argument(
    "--account", required=True, type=str, help="The Onna account name"
)
argparser.add_argument(
    "--account_url",
    required=True,
    type=str,
    help="The URL of your account, e.g https://company.onna.io or https://enterprise.onna.com",
)
argparser.add_argument(
    "--from_date",
    type=str,
    help="Start date. Most date formats are accepted",
)
argparser.add_argument(
    "--to_date",
    type=str,
    help="End date. Most date formats are accepted",
)
argparser.add_argument(
    "--container", required=False, default="rel0", help="name of the account container"
)
argparser.add_argument("--datasources", nargs="+", help="list of datasource ids")

argparser.add_argument(
    "--list_datasources",
    required=False,
    action="store_true",
    help="Fetch Datasource ids to include in the preservation",
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


def open_file_and_parse(file_path):
    with open(file_path, "r") as f:
        text = f.read()
    json_text = json.loads(text)
    return json_text


def open_file_and_get_lines(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def write_array_of_arrays_to_csv(array_info, output_file):
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(array_info)


def write_array_to_file(array_info, output_file):
    with open(output_file, "w", newline="\n", encoding="utf8") as f:
        for x in array_info:
            f.write(x)
            f.write("\r\n")


def verification_request(emails, token, account_url):

    url = f"{account_url}/@identitiesEmails"

    payload = json.dumps(emails)

    headers = {
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(response.status_code)
        return None


def parse_response(response):

    found_emails = []
    not_found_emails = []
    for account in response:
        if account.get("found") is True:
            found_emails.append(account.get("email"))
        else:
            not_found_emails.append(account.get("email"))

    return found_emails, not_found_emails


# Step 1
# Verify emails have identities


def verify_emails(token, account_url):

    matters_and_emails = open_file_and_get_lines("matters_emails.csv")

    matters_dict = dict()
    emails_dict = dict()

    for line in matters_and_emails:
        info = line.split(",")
        matter_name = info[0]
        email_address = info[1]

        if matter_name in matters_dict:
            existing_users = matters_dict[matter_name]["emails"]
            existing_users.append(email_address)
        else:
            matters_dict[matter_name] = {"emails": [email_address]}

        if info[1] in emails_dict:
            existing_matters = emails_dict[info[1]]
            existing_matters.append(matter_name)
        else:
            emails_dict[email_address] = [matter_name]

    # Batch email requests into groups of 1000
    email_batches = chunks(list(emails_dict.keys()), 1000)
    all_found_users = []
    all_not_found_users = []

    for email_batch in email_batches:
        verification_response = verification_request(email_batch, token, account_url)
        if verification_response is not None:
            found_users, not_found_users = parse_response(verification_response)
        else:
            print("invalid verification response")
            found_users = []
            not_found_users = []
        all_found_users.extend(found_users)
        all_not_found_users.extend(not_found_users)

    # Write file with not found users and matters
    not_found_array = [["matter", "email"]]
    for user in all_not_found_users:
        user_matters = emails_dict[user]
        for um in user_matters:
            not_found_array.append([um, user])

    write_array_of_arrays_to_csv(not_found_array, "Users Not Found.csv")

    return all_found_users, emails_dict, matters_dict


def get_email_identities(email_addresses, account_url, token):

    url = f"{account_url}/@frontsearch"

    payload = (
        '{"advanced":{"and":[{"in":[{"var":"type_name"},["RealIdentity"]]},{"in":[{'
        '"var":"from_mail.keyword"},' + json.dumps(email_addresses) + "]"
        '}]},"from":0,"sort":{"field":"title.keyword","direction":"asc"},"includes":["title",'
        '"from_mail"],"size":' + str(len(email_addresses)) + "} "
    )
    headers = {"authorization": f"Bearer {token}", "content-type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def parse_email_identities(email_identities_resp):
    email_identities_dict = dict()
    for member in email_identities_resp["member"]:
        if member["from_mail"] not in email_identities_dict:
            email_identities_dict[member["from_mail"]] = member["@uid"]

    return email_identities_dict


def create_preservation(
    preservation_name, identities, sources, from_date, to_date, token, account_url
):

    preservation_id = preservation_name.lower().replace(" ", "-")
    preservation_id = preservation_id.replace(".", "")

    url = f"{account_url}/workspaces"

    raw_payload = {
        "id": preservation_id,
        "@type": "Workspace",
        "title": preservation_name,
        "legal_hold": {
            "query": {
                "advanced": {
                    "and": [
                        {"in": [{"var": "parent_datasource.uuid"}, sources]},
                        {"in": [{"var": "identity-member"}, identities]},
                    ]
                }
            }
        },
    }
    if from_date is not None:
        raw_payload["legal_hold"]["query"]["advanced"]["and"].append(
            {">": [{"var": "date_modified"}, from_date]}
        )

    if to_date is not None:
        raw_payload["legal_hold"]["query"]["advanced"]["and"].append(
            {"<": [{"var": "date_modified"}, to_date]}
        )

    payload = json.dumps(raw_payload)

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 201:
        trigger_smart_action(response.json(), token)


def trigger_smart_action(response, token):

    workspace_url = response.get("@id", None)
    if workspace_url is not None:
        url = f"{workspace_url}/@smartactionCheck"

        payload = "{}"
        headers = {"authorization": f"Bearer {token}"}

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            print("scheduled")


def chunks(items, n):
    final = [items[i * n : (i + 1) * n] for i in range((len(items) + n - 1) // n)]
    return final


def get_slack_enterprise_sources(token, account_url):
    """Parse only the Enterprise Slack sources to a CSV with the Title, creation date, and UUID"""
    url = f"{account_url}/@data?types=SlackEDatasource"

    payload = {}
    headers = {
        "authorization": f"Bearer {token}",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        sources_array = []
        sources = response.json()
        for source in sources["updates"]:
            sources_array.append(
                [source["title"], source["@uid"], source["creation_date"]]
            )

        write_array_of_arrays_to_csv(sources_array, "Slack Enterprise Sources.csv")


def main():
    try:
        from_date = int(parse(args.from_date).timestamp())
    except (TypeError, ValueError):
        from_date = None
    try:
        to_date = int(parse(args.to_date).timestamp())
    except (TypeError, ValueError):
        to_date = None

    username = args.username
    password = args.password
    account = args.account
    base_url = args.account_url
    container = args.container

    account_url = f"{base_url}/api/{container}/{account}"

    auth_code_url = f"{account_url}/@oauthgetcode?client_id=canonical&scope={account}"
    code = auth_code(auth_code_url)
    token = auth_token(code, username, password, account, base_url)

    if args.list_datasources:
        get_slack_enterprise_sources(token, account_url)
        sys.exit(0)

    datasource_ids = args.datasources

    print("starting to verify emails")
    emails, emails_to_matters, matters_info = verify_emails(token, account_url)
    print("starting to get identities")
    email_identities_response = get_email_identities(emails, account_url, token)

    if email_identities_response is not None:
        email_identities_dictionary = parse_email_identities(email_identities_response)
    else:
        return

    for matter in matters_info.keys():
        matter_emails = matters_info[matter]["emails"]

        matter_identities = []
        for email in matter_emails:
            if email in email_identities_dictionary:
                matter_identities.append(email_identities_dictionary[email])

        matters_info[matter]["identities"] = matter_identities

    data_source_ids = datasource_ids

    for matter in matters_info.keys():
        matters_info[matter]["sources"] = data_source_ids

    matters_to_create = []
    for matter in matters_info.keys():
        matters_to_create.append(
            [
                matter,
                len(matters_info[matter]["sources"]),
                len(matters_info[matter]["identities"]),
                len(matters_info[matter]["emails"]),
            ]
        )
    write_array_of_arrays_to_csv(matters_to_create, "matters_to_create.csv")

    print("creating preservations")
    count = 0
    for matter in matters_info.keys():
        count += 1
        print(f"creating {str(count)} of {str(len(matters_info))}")
        sources = matters_info[matter]["sources"]
        identities = matters_info[matter]["identities"]
        # from_date = None
        # to_date = None

        create_preservation(
            matter,
            identities,
            sources,
            from_date,
            to_date,
            token,
            account_url,
        )


if __name__ == "__main__":
    args = argparser.parse_args()
    main()
