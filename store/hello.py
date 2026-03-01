# plugins/hello.py
def run(args):
    print("👋 Hello from VOR plugin!")
    if args:
        print("Args received:", args)
