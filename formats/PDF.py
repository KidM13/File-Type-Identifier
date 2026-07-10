def validate_pdf(data):
    if not data.startswith(b"%PDF"):
        return False

    if b"%%EOF" not in data:
        return False

    return True