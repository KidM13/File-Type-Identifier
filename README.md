# TrueType - File Type Identifier

## Overview

TrueType is a command-line file identification tool written in Python. It identifies files using magic number signatures instead of relying on file extensions. The tool can detect renamed files, perform basic format validation for supported file types, and report the signature used during identification.

## Features

* Detect file types using magic numbers.
* Compare detected type with the file extension.
* Validate the internal structure of supported formats.
* Display the matched file signature and its offset.
* Signature database stored in JSON for easy extension.
* Modular architecture for future enhancements.

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
├── signatures/
├── formatter.py
├── analysis_result.py
├── main.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/KidM13/File-Type-Identifier.git
cd File-Type-Identifier
```

Python 3.11 or later is recommended.

## Usage

Analyze a file:

```bash
python main.py <file>
```

Specify the number of bytes to read:

```bash
python main.py <file> --bytes 32
```

Enable verbose output:

```bash
python main.py <file> --verbose
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

* Additional format validators.
* JSON report export.
* Graphical user interface.
* Unit tests.
* Package distribution through pip.

## License

MIT License.
