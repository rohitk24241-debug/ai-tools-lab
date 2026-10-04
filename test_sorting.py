from sorting import bubble_sort


def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]


def test_empty_list():
    assert bubble_sort([]) == []


def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
