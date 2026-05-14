import argparse
import os
from core.file_reader import read_header
from core.signature_engine import detect_file_type
def main():
    parser = argparse.ArgumentParser(description=' truetype - file type identifier')
    parser.add_argument('file', help='path to the file to analyze')
    parser.add_argument('--verbose', '-v', action='store_true', help='enable verbose output')
    parser.add_argument("--bytes", type=int, default=16)
    args = parser.parse_args()
    no=args.bytes
    file_path = os.path.abspath(args.file)
    _, ext = os.path.splitext(file_path)

    ext = ext.lower().replace(".", "")
    if not os.path.isfile(file_path):
        print("invalid file")
        return
    header= read_header(file_path,no)
    detected_type = detect_file_type(header)
    print(f"detected file type: {detected_type}")

    if args.verbose:
        print("verbose mode enabled")
        print(f"analyzing file: {args.file}")

if __name__ == "__main__":
    main()