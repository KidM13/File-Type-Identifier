import argparse
import os

from core.file_reader import read_header
from core.signature_engine import (
    EXTENSION_MAP,
    detect_file_type,
    scan_signatures,
)
from formats.PNG import validate_png
from core.analayzer import FileAnalyzer


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

    
    # creating an instance of fileanaylzer
    analyzer = FileAnalyzer(args.file)

    # analyzing the file
    analyzer.analyze()

    #generating the report
        
    

if __name__ == "__main__":
    main()