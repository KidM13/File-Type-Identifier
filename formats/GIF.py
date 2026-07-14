def validate_gif(data: bytes) -> bool:
    """
    Validate a GIF file.
    """

    if not (
        data.startswith(b"GIF87a")
        or data.startswith(b"GIF89a")
    ):
        return False

    if not data.endswith(b"\x3B"):
        return False

    return True