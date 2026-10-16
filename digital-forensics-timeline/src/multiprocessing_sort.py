from multiprocessing import Pool, cpu_count
from typing import TypeVar

from src.merge_sort import merge_sort
from src.models import ForensicEvent

T = TypeVar("T")


def sort_chunk(
    chunk: list[T],
    key_name: str | None = None,
) -> list[T]:
    """Sort one chunk in a worker process."""
    if key_name is None:
        return merge_sort(chunk)

    return merge_sort(
        chunk,
        key=lambda item: getattr(item, key_name),
    )


def merge_sorted_chunks(
    chunks: list[list[T]],
    key_name: str,
) -> list[T]:
    """Merge multiple sorted chunks into one sorted list."""
    result: list[T] = []

    for chunk in chunks:
        result = merge_sort(
            result + chunk,
            key=lambda item: getattr(item, key_name),
        )

    return result


def parallel_sort_events(
    events: list[ForensicEvent],
) -> list[ForensicEvent]:
    """Sort forensic events using multiprocessing."""
    if len(events) <= 1:
        return events.copy()

    workers = min(cpu_count(), len(events))

    chunk_size = (len(events) + workers - 1) // workers

    chunks = [
        events[i : i + chunk_size]
        for i in range(0, len(events), chunk_size)
    ]

    with Pool(processes=workers) as pool:
        sorted_chunks = pool.starmap(
            sort_chunk,
            [(chunk, "timestamp") for chunk in chunks],
        )

    return merge_sorted_chunks(sorted_chunks, "timestamp")