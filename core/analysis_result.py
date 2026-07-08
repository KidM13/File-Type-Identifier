from dataclasses import dataclass
@dataclass
class AnalysisResult:
    file_path: str
    extension: str
    detected_type: str
    expected_type: str
    status: str
    validation: bool |None
    matches: list[dict]# will add signature matches as a list of dictionaries