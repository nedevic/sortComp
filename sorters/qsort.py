import random
from copy import copy
from typing import List

__all__ = ['qsort_3_colors']


def qsort_3_colors(arr: List[int]):
    arr = copy(arr)

    def sorter(left: int, right: int):
        if left >= right:
            return

        rand_index = random.randint(left, right)
        pivot = arr[rand_index]

        left_ptr = left
        right_ptr = right
        mid_ptr = left

        while mid_ptr <= right_ptr:
            if arr[mid_ptr] < pivot:
                arr[left_ptr], arr[mid_ptr] = arr[mid_ptr], arr[left_ptr]
                left_ptr += 1
            elif arr[mid_ptr] > pivot:
                arr[right_ptr], arr[mid_ptr] = arr[mid_ptr], arr[right_ptr]
                right_ptr -= 1
                # we want to remain on the same position with mid
                # after swapping with the right side
                mid_ptr -= 1
            mid_ptr += 1

        sorter(left, left_ptr - 1)
        sorter(mid_ptr, right)

    sorter(0, len(arr) - 1)
    return arr
