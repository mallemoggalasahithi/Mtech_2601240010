from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")


def merge(
    left: list[T],
    right: list[T],
    key: Callable[[T], Any],
) -> list[T]:
    """Merge two sorted lists using a comparison key."""
    result: list[T] = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(
    items: list[T],
    key: Callable[[T], Any] | None = None,
) -> list[T]:
    """Sort a list using Merge Sort."""

    if len(items) <= 1:
        return items.copy()

    if key is None:
        key = lambda item: item

    middle = len(items) // 2

    left = merge_sort(items[:middle], key)
    right = merge_sort(items[middle:], key)

    return merge(left, right, key)