import argparse
import os

import report

from core.analyzer import FileAnalyzer
from reporting import formatter


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
    analyzer = FileAnalyzer(args.file,
                            args.bytes
    )
    

    # analyzing the file
    analyzer.analyze()

    #generating the report
    print(formatter.generate_report(analyzer.results))
        
    

if __name__ == "__main__":
    main()