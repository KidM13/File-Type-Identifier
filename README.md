# TrueType - File Type Identifier

## Overview

TrueType is a command-line file identification tool written in Python. It identifies files using magic number signatures instead of relying on file extensions. The tool can detect renamed files, perform basic format validation for supported file types, and report the signature used during identification.

## Features

- Detect file types using magic number signatures.
- Compare detected type with the file extension.
- Validate the internal structure of supported formats.
- Display the matched signature and its offset.
- Identify renamed files.
- JSON-based signature database for easy extension.
- Packaged as a command-line application.

## Supported Formats

* PNG
* JPEG
* PDF
* ZIP
* GIF
* BMP
* WAV
* AVI
* MP3
* ELF
* EXE

Validation is implemented for selected formats and can be extended by adding new validators.

## Project Structure

```
File-Type-Identifier/
├── core/
├── formats/
├── reporting/
├── tests/
├── cli.py
├── pyproject.toml
├── README.md
└── LICENSE
```

## Installation

Clone the repository:

```bash
git clone https://github.com/KidM13/File-Type-Identifier.git
cd File-Type-Identifier
```

Install the project in editable mode:

```bash
pip install -e .
```

Python 3.11 or later is required.

## Usage

Analyze a file:

```bash
truetype <file>
```

Specify the number of header bytes:

```bash
truetype <file> --bytes 32
```

Enable verbose output:

```bash
truetype <file> --verbose
```

Display help:

```bash
truetype --help
```

## Example Output

```
========================================
TrueType File Analysis Report
========================================

File: image.png
Extension: png

Detected Type: PNG
Expected Type: PNG

Status: MATCH
Validation: VALID

Matched Signature: 89504E470D0A1A0A (offset 0)
```

## Future Improvements

- Additional file format validators.
- Recursive archive analysis.
- JSON and XML report export.
- Unit test suite.
- Graphical user interface.

## License

MIT License.
