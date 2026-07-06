from dataclasses import dataclass
@dataclass
class analysis_result:
    file_path: str
    detected_type: str
    expected_type: str
    status: str
    is_valid: str
    matches: list