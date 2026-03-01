# plugins/size_report.py
import os

def run(args):
    total = 0
    for dirpath, dirnames, filenames in os.walk("."):
        for f in filenames:
            if f in [".vorconfig", ".vorignore"] or f.endswith(".zip"):
                continue
            total += os.path.getsize(os.path.join(dirpath, f))
    print(f"📦 Current repo size: {total/1024:.2f} KB")
