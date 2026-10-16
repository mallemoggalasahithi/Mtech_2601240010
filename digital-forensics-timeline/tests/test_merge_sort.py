from src.merge_sort import merge_sort


def test_merge_sort_numbers():
    numbers = [38, 27, 43, 3, 9, 82, 10]

    result = merge_sort(numbers)

    assert result == [3, 9, 10, 27, 38, 43, 82]


def test_merge_sort_empty_list():
    assert merge_sort([]) == []


def test_merge_sort_single_item():
    assert merge_sort([5]) == [5]


def test_merge_sort_already_sorted():
    numbers = [1, 2, 3, 4, 5]

    assert merge_sort(numbers) == numbers