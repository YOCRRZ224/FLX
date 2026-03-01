# plugins/latest_log.py
import json, requests

def run(args):
    server = "http://127.0.0.1:2240"
    with open(".vorconfig") as f:
        repo = json.load(f)["repo"]
    r = requests.get(f"{server}/log/{repo}")
    if r.status_code == 200:
        log = r.json()
        if log:
            last = log[-1]
            print(f"📝 Last commit: {last['version']} - {last.get('message','No message')}")
        else:
            print("ℹ️ No commits yet")
    else:
        print("❌ Could not fetch log")
