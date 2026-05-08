def read_header(file_path, num_bytes=16):
    with open(file_path, "rb") as f:
        return f.read(num_bytes)