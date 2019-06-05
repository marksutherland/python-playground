"""Sorting algorithms for demonstrating test libraries."""
from typing import List


def _choose_pivot(int_list):
    return int(len(int_list) / 2)


def quicksort(int_list: List[int]) -> List[int]:
    """Sort `int_list` with the quicksort algorithm."""
    if len(int_list) <= 1:
        return int_list
    if len(int_list) == 2:
        if int_list[1] >= int_list[0]:
            return int_list
        else:
            return list(reversed(int_list))

    pivot_index = _choose_pivot(int_list)
    pivot = int_list.pop(pivot_index)
    return [
        *quicksort([x for x in int_list if x < pivot]),
        pivot,
        *quicksort([x for x in int_list if x >= pivot]),
    ]


def inplace_quicksort(int_list: List[int]) -> List[int]:
    """Sort `int_list` with the quicksort algorithm in place."""

    def _quicksort(int_list: List[int], start: int, end: int):
        if end - start > 0:
            pivot_index = start
            pivot, left, right = int_list[pivot_index], start, end
            while left <= right:
                while int_list[left] < pivot:
                    left += 1
                while int_list[right] > pivot:
                    right -= 1
                if left <= right:
                    int_list[left], int_list[right] = int_list[right], int_list[left]
                    left += 1
                    right -= 1
            _quicksort(int_list, start, right)
            _quicksort(int_list, left, end)

    _quicksort(int_list, 0, len(int_list) - 1)
