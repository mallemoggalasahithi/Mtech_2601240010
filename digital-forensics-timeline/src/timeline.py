from src.merge_sort import merge_sort
from src.models import ForensicEvent
from src.multiprocessing_sort import parallel_sort_events
from src.parsers import parse_log_file


class TimelineBuilder:
    """Build chronological forensic timelines."""

    def __init__(self, log_files: list[str]):
        self.log_files = log_files

    def load_events(self) -> list[ForensicEvent]:
        """Load events from all log files."""
        events: list[ForensicEvent] = []

        for file_path in self.log_files:
            events.extend(parse_log_file(file_path))

        return events

    def build(self, events: list[ForensicEvent]) -> list[ForensicEvent]:
        """Build timeline using Merge Sort."""
        return merge_sort(
            events,
            key=lambda event: event.timestamp,
        )

    def build_parallel(
        self,
        events: list[ForensicEvent],
    ) -> list[ForensicEvent]:
        """Build timeline using multiprocessing."""
        return parallel_sort_events(events)


def build_timeline(events: list[ForensicEvent]) -> list[ForensicEvent]:
    """Build a chronological forensic timeline."""
    return merge_sort(events, key=lambda event: event.timestamp)


def build_parallel_timeline(
    events: list[ForensicEvent],
) -> list[ForensicEvent]:
    """Build a chronological timeline using multiprocessing."""
    return parallel_sort_events(events)


def get_all_events(log_files: list[str]) -> list[ForensicEvent]:
    """Read events from multiple log files."""
    builder = TimelineBuilder(log_files)
    return builder.load_events()