import requests

url = "https://lolrmm.io/api/rmm_tools.json"

response = requests.get(url)
response.raise_for_status()

data = response.json()

installation_paths = []

for item in data:
    details = item.get("Details", {})
    paths = details.get("InstallationPaths")
    
    if isinstance(paths, list):
        # Only keep paths that contain '.exe'
        exe_paths = [path for path in paths if ".exe" in path.lower()]
        installation_paths.extend(exe_paths)

# Write filtered paths to file
with open("installation_paths.txt", "w") as file:
    for path in installation_paths:
        file.write(path + "\n")

print("Filtered .exe paths written to 'installation_paths.txt'")
