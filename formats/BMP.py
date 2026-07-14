def validate_bmp(data: bytes) -> bool:
    """
    Validate a BMP file.
    """

    if not data.startswith(b"BM"):
        return False

    if len(data) < 18:
        return False

    dib_size = int.from_bytes(
        data[14:18],
        "little"
    )

    return dib_size >= 40