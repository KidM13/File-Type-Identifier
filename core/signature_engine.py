import json
def load_signature():
    with open("signatures/signatures.json", "r") as f:
        return json.load(f)
