import json
from pathlib import Path


# Path to signatures.json
SIGNATURES_FILE = (
    Path(__file__).parent.parent
    / "signatures"
    / "signatures.json"
)


def load_signatures() -> list[dict]:
    

    with open(SIGNATURES_FILE, "r", encoding="utf-8") as f:
        signatures = json.load(f)

    # Convert each hex signature into bytes
    for signature in signatures:
        signature["signature"] = bytes.fromhex(signature["signature"])

    return signatures