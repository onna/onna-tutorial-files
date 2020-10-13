import asyncio
import aiohttp
import json

base_url = "https://enterprise.onna.com"
container = "container"
scope = account = "account"
auth_code_url = f"{base_url}/api/{container}/{account}/@oauthgetcode?client_id=canonical&scope={account}"
workspace_name = "workspace"
username = "you@example.com"
password = "super-secret-password"


async def auth():
    """Establish our auth token, first we authenticate with a password,
    then exchange that for a token which is used in subsequent requests"""
    async with aiohttp.ClientSession() as session:
        resp = await session.get(auth_code_url, ssl=False)
        if resp.status == 200:
            data = await resp.json()
            auth_code = data.get("auth_code")

        payload = {
            "grant_type": "user",
            "code": auth_code,
            "username": username,
            "password": password,
            "scopes": [scope],
            "client_id": "canonical",
        }
        headers = {"Accept": "application/json"}
        resp = await session.post(
            f"{base_url}/auth/oauth/get_auth_token",
            headers=headers,
            data=json.dumps(payload),
            ssl=False,
        )
        if resp.status == 200:
            jwt_token = await resp.text()
        return jwt_token
    return None


async def create_crawler_ds():
    """Create a Web Crawler datasource using our authorization token from above.
    This datasource will store the contents of the `urls` specified in the `data` variable
    below. In the last step, the call to `@sendToSpyder` activates our web crawler.
    """
    token = await auth()
    if not token:
        raise Exception
    workspace_url = f"{base_url}/api/{container}/{account}/workspaces/{workspace_name}"
    headers = {"Authorization": f"Bearer {token}"}
    async with aiohttp.ClientSession() as session:
        data = {
            "@id": f"{workspace_url}/onnacrawler",
            "@type": "CrawlerDatasource",
            "title": "Onna Web Crawler",
            "urls": ["https://confluence.cornell.edu/"],
        }
        resp = await session.post(
            workspace_url, data=json.dumps(data), headers=headers, ssl=False
        )
        data = await resp.json()
        if resp.status == 201:
            resp = await session.get(
                f"{data['@id']}/@sendToSpyder?force=true",
                headers=headers,
                ssl=False,
            )


asyncio.run(create_crawler_ds())
