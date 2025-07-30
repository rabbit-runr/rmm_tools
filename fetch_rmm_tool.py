import requests
import os

url = "https://lolrmm.io/api/rmm_tools.json"

response = requests.get(url)
response.raise_for_status()

data = response.json()

exe_filenames = set()

for item in data:
    details = item.get("Details", {})
    paths = details.get("InstallationPaths")

    if isinstance(paths, list):
        for path in paths:
            filename = os.path.basename(path).lower()

            # Filter exact .exe files (no wildcards, clean filenames only)
            if "*" not in filename and filename.endswith(".exe"):
                exe_filenames.add(filename)  # only keep filename

# Write cleaned filenames to file
with open("installation_paths.txt", "w") as file:
    for filename in sorted(exe_filenames):
        file.write(filename + "\n")

print("Cleaned .exe filenames written to 'installation_paths.txt'")
