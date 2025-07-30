import requests
import json

url = 'https://lolrmm.io/api/rmm_tools.json'
response = requests.get(url)
data = response.json()
installation_paths = data.get("InstallationPaths", [])
with open("installation_paths.txt", "w") as file:
    for path in installation_paths:
        file.write(path + "\n")
