import requests

url = 'https://lolrmm.io/api/rmm_tools.json'
data = requests.get(url).json()
paths = data.get('InstallationPaths', {}).keys()

with open("installation_paths.txt", "w") as f:
    for p in sorted(paths):
        f.write(f"{p}\n")
