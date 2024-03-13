from copy import copy
from typing import List

__all__ = ['bubble_sort']


def bubble_sort(arr: List[int]):
    arr = copy(arr)
    arr_size = len(arr)

    for left in range(0, arr_size - 1):
        for right in range(left, arr_size):
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]

    return arr
