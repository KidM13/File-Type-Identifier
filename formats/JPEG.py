def validate_jpeg(data):
    """
    Validate a JPEG file.
    """

    if not data.startswith(b"\xFF\xD8"):
        return False

    if not data.endswith(b"\xFF\xD9"):
        return False

    return True