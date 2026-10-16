from pathlib import Path

from src.exporters import export_to_csv, export_to_json
from src.filters import (
    filter_by_severity,
    filter_by_user,
    search_events,
)
from src.timeline import build_timeline, get_all_events

LOG_FILES = [
    "data/system.log",
    "data/application.log",
    "data/browser.log",
    "data/auth.log",
]


def display_events(events):
    """Display forensic events in chronological order."""
    print("\nFORENSIC TIMELINE")
    print("-" * 100)

    for event in events:
        print(
            f"{event.timestamp} | "
            f"{event.source:<12} | "
            f"{event.event_type:<18} | "
            f"{event.user:<8} | "
            f"{event.severity:<8} | "
            f"{event.description}"
        )

    print("-" * 100)
    print(f"Total events: {len(events)}")


def main():
    """Run the Digital Forensics Timeline Builder."""
    print("=" * 60)
    print("DIGITAL FORENSICS TIMELINE BUILDER")
    print("=" * 60)

    events = get_all_events(LOG_FILES)

    print(f"\nLoaded {len(events)} events from {len(LOG_FILES)} log files.")

    timeline = build_timeline(events)

    display_events(timeline)

    output_directory = Path("output")
    output_directory.mkdir(exist_ok=True)

    csv_file = output_directory / "forensic_timeline.csv"
    json_file = output_directory / "forensic_timeline.json"

    export_to_csv(timeline, csv_file)
    export_to_json(timeline, json_file)

    print("\nExport completed:")
    print(f"CSV : {csv_file}")
    print(f"JSON: {json_file}")

    warning_events = filter_by_severity(timeline, "WARNING")
    print(f"\nWARNING events: {len(warning_events)}")

    user_events = filter_by_user(timeline, "user1")
    print(f"user1 events: {len(user_events)}")

    search_results = search_events(timeline, "confidential")
    print(f"Search results for 'confidential': {len(search_results)}")


if __name__ == "__main__":
    main()