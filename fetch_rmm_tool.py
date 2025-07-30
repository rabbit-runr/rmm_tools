import requests

url = "https://lolrmm.io/api/rmm_tools.json"

response = requests.get(url)
response.raise_for_status()

data = response.json()

installation_paths = []

for item in data:
    details = item.get("Details", {})
    paths = details.get("InstallationPaths")
    
    # Make sure paths is a list before extending
    if isinstance(paths, list):
        exe_paths = [path for path in paths if ".exe" in path.lower()]
        installation_paths.extend(exe_paths)

# Write to file
with open("installation_paths.txt", "w") as file:
    for path in installation_paths:
        file.write(path + "\n")

print("Installation paths written to 'installation_paths.txt'")
