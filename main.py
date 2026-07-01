import argparse
import os

from core.file_reader import read_header
from core.signature_engine import (
    EXTENSION_MAP,
    detect_file_type,
    scan_signatures,
)
from formats.PNG import validate_png


def main():
    
    # Parse command-line arguments
    
    parser = argparse.ArgumentParser(
        description="TrueType - File Type Identifier"
    )

    parser.add_argument(
        "file",
        help="Path to the file to analyze"
    )

    parser.add_argument(
        "--bytes",
        type=int,
        default=16,
        help="Number of header bytes to read"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    
    # Resolve and validate file path
    
    file_path = os.path.abspath(args.file)

    if not os.path.isfile(file_path):
        print("Error: Invalid file.")
        return

    
    # Read file
    
    header = read_header(file_path, args.bytes)

    with open(file_path, "rb") as f:
        data = f.read(4096)

    
    # Detect file type
    
    detected_type = detect_file_type(header)

    
    # Extension analysis
    
    _, ext = os.path.splitext(file_path)
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

    if detected_type == "PNG":
        is_valid = validate_png(data)

    
    # Embedded signature scan
    
    matches = scan_signatures(data)

    
    # Report
    
    print(f"File: {file_path}")
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

    
    # Verbose output
    if args.verbose:
        print("\nVerbose Mode")
        print(f"Header Bytes: {header}")
        print(f"Hex: {' '.join(f'{b:02X}' for b in header)}")
        print(f"Bytes Requested: {args.bytes}")


if __name__ == "__main__":
    main()