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

    if isinstance(paths, list):
        for path in paths:
            filename = os.path.basename(path).lower()

            # Keep only exact .exe files without wildcards
            if "*" not in filename and filename.endswith(".exe"):
                installation_paths.append(filename)  # just the filename, not full path

# Write cleaned filenames to file
with open("installation_paths.txt", "w") as file:
    for filename in sorted(set(installation_paths)):
        file.write(filename + "\n")

print("Cleaned .exe filenames written to 'installation_paths.txt'")
