import yaml
import sys
import os

preview_mode = "--preview" in sys.argv
print(f"✅ PREVIEW MODE: {preview_mode}")

# Load gallery YAML only if not in preview
if not preview_mode:
    gallery_path = "gallery/notebook_gallery.yaml"
    if os.path.exists(gallery_path):
        print("✅ Loading existing notebook_gallery.yaml")
        with open(gallery_path) as f:
            gallery = yaml.safe_load(f)
    else:
        print("⚠️ notebook_gallery.yaml does not exist – creating new structure")
        gallery = {"domains": {}}

# Load and print issue body
with open('issue_body.txt') as f:
    body = f.read()

print("Full Issue Body:")
print(body)

# Parse issue fields
fields = {
    "Repository URL": "",
    "Cookbook Title": "",
    "Short Description": "",
    "Thumbnail Image URL": "",
    "Root Path Name": ""
}

lines = body.splitlines()
current_label = None

for line in lines:
    line = line.strip().lstrip("#").strip()
    if line in fields:
        current_label = line
    elif current_label and line:
        fields[current_label] = line
        current_label = None

repo_url = fields["Repository URL"]
title = fields["Cookbook Title"]
description = fields["Short Description"]
thumbnail = fields["Thumbnail Image URL"]
root_path = fields["Root Path Name"]

print(f"🔍 Extracted Fields:")
print(f"→ Repo URL     : {repo_url}")
print(f"→ Title        : {title}")
print(f"→ Description  : {description}")
print(f"→ Thumbnail    : {thumbnail}")
print(f"→ Root Path    : {root_path}")

# Abort if root path is missing
if not root_path:
    print(" ERROR: Root Path could not be extracted – aborting.")
    raise ValueError("Root Path konnte nicht extrahiert werden – Abbruch.")

# Write to gallery YAML (only in production mode)
if not preview_mode:
    print(f"Writing entry to notebook_gallery.yaml for root path: {root_path}")
    gallery['domains'][root_path] = {
        'title': title,
        'branch': 'main',
        'root_path': root_path,
        'description': description,
        'thumbnail': thumbnail,
        'url': f"https://katharinastarzer21.github.io/gallery_web/cookbooks/{root_path}/index.html"
    }

    with open('notebook_gallery.yaml', 'w') as f:
        yaml.dump(gallery, f, sort_keys=False)
    print("notebook_gallery.yaml updated successfully")

# Export env vars
with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    env_file.write(f"REPO_URL={repo_url}\n")
    env_file.write(f"ROOT_PATH={root_path}\n")
print("Environment variables exported for GitHub Actions")
