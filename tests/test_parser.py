from app.parser import parse_line


def test_parse_valid_line():
    line = "2026-11-21 10:00:00 [ERROR] payments: Failed to connect to database"
    result = parse_line(line)
    assert result == {
        "timestamp": "2026-11-21 10:00:00",
        "severity": "ERROR",
        "service": "payments",
        "message": "Failed to connect to database",
    }


def test_parse_invalid_line():
    assert parse_line("this is not a log line") is None