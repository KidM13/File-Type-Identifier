def validate_exe(data: bytes) -> bool:
    """
    Validate a Windows PE executable.
    """

    if not data.startswith(b"MZ"):
        return False

    if len(data) < 64:
        return False

    pe_offset = int.from_bytes(
        data[60:64],
        "little"
    )

    if pe_offset + 4 > len(data):
        return False

    return data[pe_offset:pe_offset + 4] == b"PE\x00\x00"