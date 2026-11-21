from datetime import datetime, timedelta

ERROR_THRESHOLD = 3
TIME_WINDOW = timedelta(minutes=1)

def find_incidents(entries: list[dict]) -> list[dict]:
    errors_by_service: dict[str, list[datetime]] = {}
    incidents = []

    for entry in entries:
        if entry["severity"] != "ERROR":
            continue

        service = entry["service"]
        timestamp = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S")

        errors_by_service.setdefault(service, []).append(timestamp)
        recent_errors = [t for t in errors_by_service[service] if timestamp - t <= TIME_WINDOW]
        errors_by_service[service] = recent_errors

        if len(recent_errors) >= ERROR_THRESHOLD:
            incidents.append({
                "service": service,
                "error_count": len(recent_errors),
                "detected_at": entry["timestamp"],
            })

    return incidents

if __name__ == "__main__":
    sample_entries = [
        {"timestamp": "2026-11-21 10:00:00", "severity": "ERROR", "service": "payments", "message": "x"},
        {"timestamp": "2026-11-21 10:00:10", "severity": "INFO", "service": "auth", "message": "ok"},
        {"timestamp": "2026-11-21 10:00:20", "severity": "ERROR", "service": "payments", "message": "x"},
        {"timestamp": "2026-11-21 10:00:30", "severity": "ERROR", "service": "payments", "message": "x"},
    ]
    for incident in find_incidents(sample_entries):
        print(incident)