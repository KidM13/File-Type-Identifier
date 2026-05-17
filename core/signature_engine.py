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
            return  file_type

    return "Unknown"

def scan_signatures(data):
    matches =[]
    for file_type,signature in SIGNATURES.items():
        offset=data.find(signature)

        if offset != -1:
            matches.append({
                "type": file_type,
                "offset": offset
            })
    return matches