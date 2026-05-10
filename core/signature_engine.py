SIGNATURES = {
    "PNG": b"\x89PNG",
    "JPG": b"\xFF\xD8\xFF",
    "PDF": b"%PDF",
    "ZIP": b"PK\x03\x04",
    "EXE": b"MZ"
}
def detect_file_type(header):
    for file_type, signature in SIGNATURES.items():

        if header.startswith(signature):
            return file_type

    return "Unknown"