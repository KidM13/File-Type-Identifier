def validate_png(data):

    if b'IHDR' not in data:
        return False

    if b'IEND' not in data:
        return False

    return True