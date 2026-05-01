import argparse
def main():
    parser = argparse.ArgumentParser(description=' truetype - file type identifier')
    parser.add_argument('file', help='path to the file to analyze')
    args = parser.parse_args()
    print(f"analyzing file: {args.file}")

if __name__ == "__main__":
    main()