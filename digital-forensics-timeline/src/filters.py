from src.models import ForensicEvent


def filter_by_user(
    events: list[ForensicEvent],
    user: str,
) -> list[ForensicEvent]:
    """Return events belonging to a specific user."""
    return [event for event in events if event.user == user]


def filter_by_severity(
    events: list[ForensicEvent],
    severity: str,
) -> list[ForensicEvent]:
    """Return events with a specific severity."""
    return [
        event
        for event in events
        if event.severity.upper() == severity.upper()
    ]


def filter_by_source(
    events: list[ForensicEvent],
    source: str,
) -> list[ForensicEvent]:
    """Return events from a specific source."""
    return [
        event
        for event in events
        if event.source.upper() == source.upper()
    ]


def filter_by_event_type(
    events: list[ForensicEvent],
    event_type: str,
) -> list[ForensicEvent]:
    """Return events with a specific event type."""
    return [
        event
        for event in events
        if event.event_type.upper() == event_type.upper()
    ]


def search_events(
    events: list[ForensicEvent],
    keyword: str,
) -> list[ForensicEvent]:
    """Search event descriptions and event types."""
    keyword = keyword.lower()

    return [
        event
        for event in events
        if keyword in event.description.lower()
        or keyword in event.event_type.lower()
    ]