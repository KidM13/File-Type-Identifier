from core.file_reader import read_header
from formats.PDF import validate_pdf
from formats.PNG import validate_png
from analysis_result import AnalysisResult
import os
VALIDATORS={
    "PNG":validate_png, #this will grow later
    "PDF":validate_pdf,
}
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

        validator = VALIDATORS.get(detected_type)

        if validator:
          is_valid = validator(data)
        # Embedded signature scan
        matches = scan_signatures(data)

        self.results = AnalysisResult(
    file_path=self.file_path,
    detected_type=detected_type,
    expected_type=expected_type,
    status=status,
    validation=is_valid,
    matches=matches,
)
        def generate_report(results):
            print("========================================\nTrueType File Analysis Report\n========================================")
            print(f"File:\n{self.file_path}")
            print(f"Detected Type: \n{detected_type}")
            print(f"Expected Type:\n")
            print(f"Status: \n{status}")
            if validator:
                print(f"validation: \n{validator}")
            else:
              print(f"validation: \n INVALID")  
            print(f"Embedded Signatures:\n")
            if matches:
             for match in matches:
                print(
                    f" - {match['type']} at offset {match['offset']}"
                )
            else:
               print("None found")


        
        

