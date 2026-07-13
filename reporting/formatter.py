def generate_report(result):
    """
    Convert an AnalysisResult object
    into a formatted report string.
    """

    if result.validation is True:
        validation = "VALID"

    elif result.validation is False:
        validation = "INVALID"

    else:
        validation = "NOT CHECKED"

    report = []

    report.append("=" * 40)
    report.append("TrueType File Analysis Report")
    report.append("=" * 40)

    report.append(f"File: {result.file_path}")
    report.append(f"Extension: {result.extension}")
    report.append(f"Detected Type: {result.detected_type}")
    report.append(f"Expected Type: {result.expected_type}")
    report.append(f"Status: {result.status}")
    report.append(f"Validation: {validation}")
    if result.matched_signature is None:
     report.append("Matched Signature : None")
     report.append("Signature Offset  : N/A")
    else:
     report.append(f"Matched Signature : {result.matched_signature}")
     report.append(f"Signature Offset  : {result.signature_offset}")

    report.append("")
    report.append("Embedded Signatures:")

    if result.matches:

        for match in result.matches:
            report.append(
                f" - {match['type']} at offset {match['offset']}"
            )

    else:
        report.append("None")

    return "\n".join(report)