from src.models import ForensicEvent
from src.multiprocessing_sort import parallel_sort_events


def test_parallel_sort_events():
    events = [
        ForensicEvent(
            timestamp="2026-10-05 10:30:00",
            source="TEST",
            event_type="TEST",
            user="user1",
            description="Event 3",
            severity="INFO",
        ),
        ForensicEvent(
            timestamp="2026-10-05 10:10:00",
            source="TEST",
            event_type="TEST",
            user="user1",
            description="Event 1",
            severity="INFO",
        ),
        ForensicEvent(
            timestamp="2026-10-05 10:20:00",
            source="TEST",
            event_type="TEST",
            user="user1",
            description="Event 2",
            severity="INFO",
        ),
    ]

    result = parallel_sort_events(events)

    assert result[0].timestamp == "2026-10-05 10:10:00"
    assert result[1].timestamp == "2026-10-05 10:20:00"
    assert result[2].timestamp == "2026-10-05 10:30:00"


def test_parallel_sort_empty_list():
    assert parallel_sort_events([]) == []


def test_parallel_sort_single_event():
    event = ForensicEvent(
        timestamp="2026-10-05 10:10:00",
        source="TEST",
        event_type="TEST",
        user="user1",
        description="Single event",
        severity="INFO",
    )

    result = parallel_sort_events([event])

    assert len(result) == 1
    assert result[0] == event