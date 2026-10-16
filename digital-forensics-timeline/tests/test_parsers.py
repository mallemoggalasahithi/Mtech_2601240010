from pathlib import Path

from src.parsers import parse_log_file, parse_log_line


def test_parse_log_line():
    line = (
        "2026-10-05 10:15:32 | SYSTEM | PROCESS_START | "
        "admin | Windows Update service started | INFO"
    )

    event = parse_log_line(line)

    assert event.source == "SYSTEM"
    assert event.event_type == "PROCESS_START"
    assert event.user == "admin"
    assert event.severity == "INFO"


def test_parse_log_file():
    file_path = Path("data/system.log")

    events = parse_log_file(file_path)

    assert len(events) == 8
    assert events[0].source == "SYSTEM"
    assert events[0].user == "admin"