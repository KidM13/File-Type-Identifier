def validate_elf(data: bytes) -> bool:
    """
    Validate an ELF executable.
    """

    if not data.startswith(b"\x7FELF"):
        return False

    if data[4] not in (1, 2):
        return False

    if data[5] not in (1, 2):
        return False

    return True