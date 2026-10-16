from datetime import datetime

from src.timeline import build_timeline, get_all_events


def test_get_all_events():
    log_files = [
        "data/system.log",
        "data/application.log",
        "data/browser.log",
        "data/auth.log",
    ]

    events = get_all_events(log_files)

    assert len(events) == 32


def test_build_timeline():
    log_files = [
        "data/system.log",
        "data/application.log",
        "data/browser.log",
        "data/auth.log",
    ]

    events = get_all_events(log_files)
    timeline = build_timeline(events)

    assert len(timeline) == 32

    for i in range(len(timeline) - 1):
        assert timeline[i].timestamp <= timeline[i + 1].timestamp


def test_first_event_is_earliest():
    log_files = [
        "data/system.log",
        "data/application.log",
        "data/browser.log",
        "data/auth.log",
    ]

    events = get_all_events(log_files)
    timeline = build_timeline(events)

    assert timeline[0].timestamp == datetime(  # noqa: DTZ001
        2026,
        10,
        5,
        10,
        7,
        45,
    )