from datetime import datetime
from pathlib import Path

from src.models import ForensicEvent


def parse_log_line(line: str) -> ForensicEvent:
    """Convert one log line into a ForensicEvent object."""
    parts = [part.strip() for part in line.split("|")]

    if len(parts) != 6:
        raise ValueError(f"Invalid log format: {line}")

    timestamp = datetime.strptime(  # noqa: DTZ007
        parts[0],
        "%Y-%m-%d %H:%M:%S",
    )

    return ForensicEvent(
        timestamp=timestamp,
        source=parts[1],
        event_type=parts[2],
        user=parts[3],
        description=parts[4],
        severity=parts[5],
    )


def parse_log_file(file_path: str | Path) -> list[ForensicEvent]:
    """Read a log file and return its forensic events."""
    events: list[ForensicEvent] = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                events.append(parse_log_line(line))
            except ValueError as error:
                print(f"Skipping invalid line {line_number}: {error}")

    return events