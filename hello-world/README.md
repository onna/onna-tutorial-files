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
Download example script fro GitHub with (wget/cURL)

```shell
wget https://raw.githubusercontent.com/onna/onna-tutorial-files/master/Dogs.txt (Change that later!)
```
Change settings to $YOUR-ACCOUNT settings (Explain with example)

Activate `venv`

```shell
source .venv/bin/activate
````

`pip install -r requirements.txt`

```shell
pip install -r requirements.txt
```

Change permissions

```shell
chmod +x create-datasource.py
````

Run script

./create-datasource.py