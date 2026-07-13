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
        signature["signature_bytes"] = bytes.fromhex(
            signature["signature"])
    return signatures
# Load the database once
SIGNATURES = load_signatures()

# Build extension lookup automatically
EXTENSION_MAP = {
    signature["extension"]: signature["name"]
    for signature in SIGNATURES
}


def detect_file_type(header: bytes) -> dict | None:
    """
    Detect the file type using the loaded signatures.
    """

    for signature in SIGNATURES:

        sig = signature["signature_bytes"]
        offset = signature["offset"]

        # Make sure enough bytes were read
        if len(header) < offset + len(sig):
            continue

        if header[offset:offset + len(sig)] == sig:
            return signature

    return "None"

def scan_signatures(data: bytes) -> list[dict]:
    """
    Scan the entire file for embedded signatures.
    """

    matches = []

    for signature in SIGNATURES:

        sig = signature["signature_bytes"]

        start = 0

        while True:

            position = data.find(sig, start)

            if position == -1:
                break

            matches.append(
                {
                    "type": signature["name"],
                    "extension": signature["extension"],
                    "offset": position,
                }
            )

            start = position + 1

    return matches