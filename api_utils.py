import requests

url = "https://api.github.com/repos/lgesnb/shuabu/actions/workflows/run.yml/dispatches"
headers = {
    "Authorization": "token BOJFUW2B5EFUAQDMERLUNVDIDURIG",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.post(url, headers=headers)
print(response.json())
