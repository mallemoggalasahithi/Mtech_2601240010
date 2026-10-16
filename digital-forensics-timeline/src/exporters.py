import csv
import json
from pathlib import Path

from src.models import ForensicEvent


def export_to_csv(
    events: list[ForensicEvent],
    file_path: str | Path,
) -> None:
    """Export forensic events to a CSV file."""
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "Timestamp",
                "Source",
                "Event Type",
                "User",
                "Description",
                "Severity",
            ]
        )

        for event in events:
            writer.writerow(
                [
                    event.timestamp.isoformat(sep=" "),
                    event.source,
                    event.event_type,
                    event.user,
                    event.description,
                    event.severity,
                ]
            )


def export_to_json(
    events: list[ForensicEvent],
    file_path: str | Path,
) -> None:
    """Export forensic events to a JSON file."""
    data = [
        {
            "timestamp": event.timestamp.isoformat(sep=" "),
            "source": event.source,
            "event_type": event.event_type,
            "user": event.user,
            "description": event.description,
            "severity": event.severity,
        }
        for event in events
    ]

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)