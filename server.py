from flask import Flask, request, send_file, jsonify
import os, json, time

app = Flask(__name__)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.join(BASE_PATH, "repos")
STORE_DIR = os.path.join(BASE_PATH, "store")

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(STORE_DIR, exist_ok=True)

print("🔥 FLX SERVER running from:", BASE_PATH)
print("📦 STORE DIR:", STORE_DIR)
def repo_dir(repo):
    return os.path.join(BASE_DIR, repo)

def log_file(repo):
    return os.path.join(repo_dir(repo), "log.json")

@app.route("/push", methods=["POST"])
def push():
    repo = request.form["repo"]
    version = request.form["version"]
    message = request.form.get("message", "No message")  # <-- new: commit message
    file = request.files["file"]

    repo_path = repo_dir(repo)
    os.makedirs(repo_path, exist_ok=True)

    save_path = os.path.join(repo_path, f"{version}.zip")
    file.save(save_path)

    # ---- LOGGING ----
    log = []
    lf = log_file(repo)
    if os.path.exists(lf):
        with open(lf) as f:
            log = json.load(f)

    log.append({
        "version": version,
        "time": time.ctime(),
        "message": message   # <-- store commit message
    })

    with open(lf, "w") as f:
        json.dump(log, f, indent=2)

    return jsonify({"status": "success", "message": "Version uploaded"})

@app.route("/pull/<repo>/<version>", methods=["GET"])
def pull(repo, version):
    path = os.path.join(BASE_DIR, repo, f"{version}.zip")
    if not os.path.exists(path):
        return jsonify({"error": "Version not found"}), 404
    return send_file(path, as_attachment=True)

@app.route("/list/<repo>", methods=["GET"])
def list_versions(repo):
    repo_path = os.path.join(BASE_DIR, repo)
    if not os.path.exists(repo_path):
        return jsonify([])
    return jsonify(os.listdir(repo_path))

# ---- NEW: LOG ENDPOINT ----
@app.route("/log/<repo>", methods=["GET"])
def get_log(repo):
    lf = log_file(repo)
    if not os.path.exists(lf):
        return jsonify([])
    with open(lf) as f:
        return jsonify(json.load(f))

@app.route("/store/list", methods=["GET"])
def store_list():
    plugins = [f.replace(".py","") for f in os.listdir(STORE_DIR) if f.endswith(".py")]
    return jsonify(plugins)


@app.route("/store/get/<plugin>", methods=["GET"])
def store_get(plugin):
    path = os.path.join(STORE_DIR, f"{plugin}.py")
    if not os.path.exists(path):
        return jsonify({"error": "Plugin not found"}), 404
    return send_file(path, as_attachment=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2240)
