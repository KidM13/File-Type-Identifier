from dataclasses import dataclass
@dataclass
class AnalysisResult:
    file_path: str
    extension: str
    detected_type: str
    expected_type: str
    status: str
    validation: bool | None
    matched_signature: str | None
    signature_offset: int | None
    matches: list# will add signature matches as a list of dictionaries