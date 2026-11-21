import random
import time
from datetime import datetime

SERVICES = ["payments", "auth", "search", "notifications"]

MESSAGES = {
    "INFO": [
        "Request completed successfully",
        "User logged in",
        "Cache refreshed",
    ],
    "WARNING": [
        "Response time above threshold",
        "Retrying request",
        "Low memory warning",
    ],
    "ERROR": [
        "Failed to connect to database",
        "Timeout while calling external service",
        "Unhandled exception in request handler",
    ],
}

# Real systems log mostly INFO, with WARNING and ERROR much rarer.
SEVERITIES = ["INFO", "WARNING", "ERROR"]
SEVERITY_WEIGHTS = [0.7, 0.2, 0.1]


def generate_log_line() -> str:
    service = random.choice(SERVICES)
    severity = random.choices(SEVERITIES, weights=SEVERITY_WEIGHTS)[0]
    message = random.choice(MESSAGES[severity])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} [{severity}] {service}: {message}"

def run(log_path: str = "app.log", interval_seconds: float = 1.0) -> None:
    print(f"Generating logs into {log_path} (Ctrl+C to stop)...")
    with open(log_path, "a", encoding="utf-8") as f:
        while True:
            line = generate_log_line()
            f.write(line + "\n")
            f.flush()
            print(line)
            time.sleep(interval_seconds)


if __name__ == "__main__":
    run()