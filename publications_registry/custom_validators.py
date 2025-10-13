from django.core.validators import RegexValidator

def validate_issue_number(issue_number):
    """
    Validates that the issue number is valid.
    Expected pattern: YYYY/NR (continuous nr) e.g. 2025/2 (67)
    """
    issue = str(issue_number)
    # Regex for pattern like: 2025/1 (11).
    regex = r"([0-9{4}]/[0-4] \([0-9]{1,3}\))"
    regex_validator = RegexValidator(regex=regex,
                                     message="Niepoprawny format.\n"
                                             "Wprowadź zgodnie ze wzorem:\n"
                                             "RRRR/NR (nr ciągły)" )

    return regex_validator(issue)
