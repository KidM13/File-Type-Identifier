from core.file_reader import read_header
class FileAnalyzer:

    def __init__(self, file_path,header_size=16):
        self.file_path = file_path
        self.header = read_header(file_path, header_size)

    def analyze(self):
        from core.signature_engine import (
            EXTENSION_MAP,
            detect_file_type,
            scan_signatures,
        )
        from formats.PNG import validate_png
        import os

        # Detect file type
        detected_type = detect_file_type(self.header)

        # Extension analysis
        _, ext = os.path.splitext(self.file_path)
        ext = ext.lower().replace(".", "")

        expected_type = EXTENSION_MAP.get(ext)

        if expected_type is None:
            expected_type = "Unknown"
            status = "UNKNOWN EXTENSION"
        elif expected_type == detected_type:
            status = "MATCH"
        else:
            status = "MISMATCH"

        # Structure validation
        is_valid = "Not Checked"

        with open(self.file_path, "rb") as f:
            data = f.read(4096)

        if detected_type == "PNG":
            is_valid = validate_png(data)

        # Embedded signature scan
        matches = scan_signatures(data)

        # Report
        print(f"File: {self.file_path}")
        print(f"Extension: {ext}")
        print(f"Detected Type: {detected_type}")
        print(f"Status: {status}")
        print(f"Structure Validation: {is_valid}")

        print("\nEmbedded Signatures:")

        if matches:
            for match in matches:
                print(
                    f" - {match['type']} at offset {match['offset']}"
                )
        else:
            print("None found")


