from src.filters import (
    filter_by_event_type,
    filter_by_severity,
    filter_by_source,
    filter_by_user,
    search_events,
)
from src.timeline import get_all_events


def get_test_events():
    log_files = [
        "data/system.log",
        "data/application.log",
        "data/browser.log",
        "data/auth.log",
    ]

    return get_all_events(log_files)


def test_filter_by_user():
    events = get_test_events()

    result = filter_by_user(events, "user1")

    assert len(result) > 0
    assert all(event.user == "user1" for event in result)


def test_filter_by_severity():
    events = get_test_events()

    result = filter_by_severity(events, "WARNING")

    assert len(result) > 0
    assert all(event.severity == "WARNING" for event in result)


def test_filter_by_source():
    events = get_test_events()

    result = filter_by_source(events, "AUTH")

    assert len(result) == 8
    assert all(event.source == "AUTH" for event in result)


def test_filter_by_event_type():
    events = get_test_events()

    result = filter_by_event_type(events, "LOGIN_FAILED")

    assert len(result) == 2
    assert all(event.event_type == "LOGIN_FAILED" for event in result)


def test_search_events():
    events = get_test_events()

    result = search_events(events, "confidential")

    assert len(result) > 0
    assert any("confidential" in event.description.lower() for event in result)