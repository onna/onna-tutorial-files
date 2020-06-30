# About

In 6 minutes you can have a functioning Python program that authenticates against your Onna account,
creates a Datasource and retrieves data from a remote location.

You can see the output of this program when you login to your Onna account.

## Requirements

Please make sure that you have all [requirements](https://developers.onna.com/install.html "Link to requirements") installed.

This example uses [Python](https://www.python.org/downloads/release/python-380/ "Official Python 3.8").

Access to the Onna API requires that you have an active account.

You can sign up for an Onna account by filling out the [registration form](https://register.onna.com/signup?trial=true "Onna trial account registration").

You should also [create a workspace](https://support.onna.com/en/articles/1151536-how-to-create-a-workspace "How to create a workspace") in your Onna account, and remember its name.

Additional `Wget`and or `cURL` for downloading the example script form GitHub.

> Note: If you do not have or want all the needed requirements installed, get the Docker container (HERE LINK TO CONTAINER)
> And here the docs about how to run the container.

## Setup

Create a directory

```shell
mkdir onna-example
````

Change into that directory and create a `venv` (Virtual Environment)

```shell
cd onna-example
python3 -m venv .venv
```

Activate `venv`

```shell
source .venv/bin/activate
```

## Install

Install requirements with pip

```shell
pip install -r requirements.txt
```

## Authentication

Before you run the script you want to make sure that your credentials are working and that everything is setup
properly.

Download the [check-auth](https://raw.githubusercontent.com/onna/onna-tutorial-files/master/hello-world/check-auth.py) script
and replace the placeholders with your credentials (username, account, etc).

Wget

```shell
wget https://raw.githubusercontent.com/onna/onna-tutorial-files/master/hello-world/check-auth.py
```

cURL

```shell
curl https://raw.githubusercontent.com/onna/onna-tutorial-files/master/hello-world/check-auth.py -o create-datasource.py
```

Change permissions of the script and run it:

```shell
chmod +x check-auth.py
./check-auth.py
```

The response should have a value for auth_code, it is required for the next leg of the authentication flow:

```shell
auth_code: xxxxx...
```

## Create A Datasource

Download [example script from GitHub](https://raw.githubusercontent.com/onna/onna-tutorial-files/master/hello-world/create-datasource.py) with (Wget/cURL)

Wget

```shell
wget https://raw.githubusercontent.com/onna/onna-tutorial-files/master/hello-world/create-datasource.py
```

cURL

```shell
curl https://raw.githubusercontent.com/onna/onna-tutorial-files/master/hello-world/create-datasource.py -o create-datasource.py
```

Change settings to $YOUR-ACCOUNT settings (Explain with example)

Change permissions

```shell
chmod +x create-datasource.py
```

Run script

```shell
./create-datasource.py
```