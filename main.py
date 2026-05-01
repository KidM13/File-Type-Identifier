import argparse
import os
def main():
    parser = argparse.ArgumentParser(description=' truetype - file type identifier')
    parser.add_argument('file', help='path to the file to analyze')
    parser.add_argument('--verbose', '-v', action='store_true', help='enable verbose output')
    args = parser.parse_args()
    if not os.path.exists(args.file):
        print(f"Error: file '{args.file}' does not exist.")
        return
    print(f"analyzing file: {args.file}")
    if args.verbose:
        print("verbose mode enabled")
        print(f"analyzing file: {args.file}")

if __name__ == "__main__":
    main()