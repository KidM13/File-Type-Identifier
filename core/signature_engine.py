SIGNATURES = {
    "PNG": b"\x89PNG",
    "JPG": b"\xFF\xD8\xFF",
    "PDF": b"%PDF",
    "ZIP": b"PK\x03\x04",
    "EXE": b"MZ"
}

EXTENSION_MAP = {
    "png": "PNG",
    "jpg": "JPG",
    "jpeg": "JPG",
    "pdf": "PDF",
    "zip": "ZIP",
    "exe": "EXE"
}
def detect_file_type(header):
    for file_type, signature in SIGNATURES.items():

        if header.startswith(signature):
            return {
    "type": file_type,
    "signature": signature.hex().upper()
}

    return "Unknown"