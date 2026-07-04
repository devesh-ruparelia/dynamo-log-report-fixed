import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
EXPECTED_REPORT = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def test_report_is_valid_json():
    """Criterion 1: The report file must be valid JSON."""
    assert REPORT_PATH.exists(), "no report.json found"
    with REPORT_PATH.open() as report_file:
        json.load(report_file)


def test_report_has_exact_keys():
    """Criterion 2: The JSON object must contain exactly the required keys."""
    with REPORT_PATH.open() as report_file:
        report = json.load(report_file)

    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report) == set(EXPECTED_REPORT)


def test_total_requests():
    """Criterion 3: total_requests must be the number of non-empty log lines."""
    with REPORT_PATH.open() as report_file:
        report = json.load(report_file)

    assert report["total_requests"] == EXPECTED_REPORT["total_requests"]


def test_unique_ips():
    """Criterion 4: unique_ips must be the number of distinct client IP addresses."""
    with REPORT_PATH.open() as report_file:
        report = json.load(report_file)

    assert report["unique_ips"] == EXPECTED_REPORT["unique_ips"]


def test_top_path():
    """Criterion 5: top_path must be the request path with the highest request count."""
    with REPORT_PATH.open() as report_file:
        report = json.load(report_file)

    assert report["top_path"] == EXPECTED_REPORT["top_path"]
