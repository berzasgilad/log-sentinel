from app.incident_rules import find_incidents


def test_detects_incident_after_threshold():
    entries = [
        {"timestamp": "2026-11-21 10:00:00", "severity": "ERROR", "service": "payments", "message": "x"},
        {"timestamp": "2026-11-21 10:00:10", "severity": "ERROR", "service": "payments", "message": "x"},
        {"timestamp": "2026-11-21 10:00:20", "severity": "ERROR", "service": "payments", "message": "x"},
    ]
    incidents = find_incidents(entries)
    assert len(incidents) == 1
    assert incidents[0]["service"] == "payments"


def test_no_incident_below_threshold():
    entries = [
        {"timestamp": "2026-11-21 10:00:00", "severity": "ERROR", "service": "payments", "message": "x"},
        {"timestamp": "2026-11-21 10:00:10", "severity": "ERROR", "service": "payments", "message": "x"},
    ]
    assert find_incidents(entries) == []