def validate_zip(data):
    """
    Validate a ZIP archive.
    """

    if not data.startswith(b"PK\x03\x04"):
        return False

    if b"PK\x05\x06" not in data:
        return False

    return True