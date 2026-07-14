def validate_wav(data: bytes) -> bool:
    """
    Validate a WAV file.
    """

    if not data.startswith(b"RIFF"):
        return False

    if data[8:12] != b"WAVE":
        return False

    return True