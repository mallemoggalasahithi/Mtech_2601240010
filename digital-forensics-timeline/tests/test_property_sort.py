from hypothesis import given
from hypothesis import strategies as st

from src.merge_sort import merge_sort


@given(st.lists(st.integers()))
def test_merge_sort_always_sorted(numbers):
    result = merge_sort(numbers)

    assert result == sorted(numbers)


@given(st.lists(st.integers()))
def test_merge_sort_preserves_length(numbers):
    result = merge_sort(numbers)

    assert len(result) == len(numbers)