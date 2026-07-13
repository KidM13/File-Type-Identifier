from core.file_reader import read_header
from formats.PDF import validate_pdf
from formats.PNG import validate_png
from formats.JPEG import validate_jpeg
from formats.ZIP import validate_zip
from core.analysis_result import AnalysisResult
from core.signature_engine import (
            EXTENSION_MAP,
            detect_file_type,
            scan_signatures,
        )
import os
VALIDATORS={
    "PNG":validate_png, #this will grow later
    "PDF":validate_pdf,
    "JPEG": validate_jpeg,
    "ZIP": validate_zip,
}
class FileAnalyzer:

    def __init__(self, file_path,header_size=16):
        self.file_path = file_path
        self.header = read_header(file_path, header_size)
        self.results = None

    def analyze(self):
        


        # Detect file type
        match = detect_file_type(self.header)

        #extracting the information we need
        if match:
         detected_type = match["name"]
         matched_signature = match["signature"].hex().upper()
         signature_offset = match["offset"]
        else:
         detected_type = "Unknown"
         matched_signature = None
         signature_offset = None

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


        with open(self.file_path, "rb") as f:
            data = f.read(4096)

        validator = VALIDATORS.get(detected_type)

        is_valid = None

        if validator:
          is_valid = validator(data)
        else:
            is_valid=None
        # Embedded signature scan
        matches = scan_signatures(data)

        # store results
        self.results = AnalysisResult(
    file_path=self.file_path,
    extension=ext,
    detected_type=detected_type,
    expected_type=expected_type,
    status=status,
    validation=is_valid,
    matched_signature=matched_signature,
    signature_offset=signature_offset,
    matches=matches,
)
        


        
        

