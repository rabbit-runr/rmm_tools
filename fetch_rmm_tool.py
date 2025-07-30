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
        filename = os.path.basename(path).lower()
            
        # Keep only exact .exe files without wildcards
        if "*" not in filename and filename.endswith(".exe"):
            installation_paths.append(path)

# Write filtered paths to file
with open("installation_paths.txt", "w") as file:
    for path in installation_paths:
        file.write(path + "\n")

print("Filtered .exe paths written to 'installation_paths.txt'")
