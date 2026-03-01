# plugins/joke.py
import requests

def run(args):
    category = "Any"

    if args:
        category = args[0]  # ex: programming, dark, pun

    url = f"https://v2.jokeapi.dev/joke/{category}?safe-mode"

    try:
        r = requests.get(url, timeout=5)
        data = r.json()

        if data.get("type") == "single":
            print("😂", data["joke"])
        else:
            print("😂", data["setup"])
            print("👉", data["delivery"])

    except Exception as e:
        print("❌ Failed to fetch joke:", e)