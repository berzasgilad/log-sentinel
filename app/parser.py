import re

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"\[(?P<severity>\w+)\] "
    r"(?P<service>\w+): "
    r"(?P<message>.+)$"
)

def parse_line(line: str) -> dict | None:
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None
    return match.groupdict()

def parse_file(log_path: str = "app.log") -> list[dict]:
    parsed = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            entry = parse_line(line)
            if entry:
                parsed.append(entry)
    return parsed


if __name__ == "__main__":
    for entry in parse_file():
        print(entry)