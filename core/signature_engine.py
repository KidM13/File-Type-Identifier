import json
def load_signature():
    with open("signatures/signatures.json", "r") as f:
        return json.load(f)

def convert_hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)
