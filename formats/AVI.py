def validate_avi(data: bytes) -> bool:
    """
    Validate an AVI file.
    """

    if not data.startswith(b"RIFF"):
        return False

    if data[8:12] != b"AVI ":
        return False

    return True