# plugins/version_count.py
import json, requests

def run(args):
    server = "http://127.0.0.1:2240"
    with open(".vorconfig") as f:
        repo = json.load(f)["repo"]
    r = requests.get(f"{server}/list/{repo}")
    if r.status_code == 200:
        print(f"📦 Total versions on server: {len(r.json())}")
    else:
        print("❌ Could not fetch versions")
