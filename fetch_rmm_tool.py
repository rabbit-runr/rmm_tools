import requests
import os

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
        for path in paths:
            if ".exe" in path.lower():
                # Normalize path and extract filename
                filename = os.path.basename(path.strip("*")).lower()
                if filename.endswith(".exe"):
                    exe_names.add(filename)

# Write to file
with open("installation_paths.txt", "w") as file:
    for name in sorted(exe_names):
        file.write(name + "\n")

print("Installation paths written to 'installation_paths.txt'")
