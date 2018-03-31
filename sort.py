from time import time

import numpy as np
from numba import jit
import math
from utils import check_sort, calc_time


@calc_time
@jit(cache=True)
def bubble_sort(arr):
    flag = True
    for i in range(len(arr) - 1, 0, -1):
        if not flag:
            break
        flag = False
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
    return arr


@calc_time
@jit(cache=True)
def select_sort(arr):
    for i in range(len(arr) - 1):
        idx = i
        for j in range(i + 1, len(arr)):
            if arr[idx] > arr[j]:
                idx = j
        arr[idx], arr[i] = arr[i], arr[idx]
    return arr


@calc_time
@jit(cache=True)
def insert_sort(arr):
    for i in range(1, len(arr)):
        idx = i
        for j in range(i - 1, -1, -1):
            if arr[idx] < arr[j]:
                arr[idx], arr[j] = arr[j], arr[idx]
                idx = j
            else:
                break
    return arr


@calc_time
@jit(cache=True)
def shell_sort(arr):
    dist = len(arr)
    while True:
        dist = dist // 3 + 1
        for i in range(dist, len(arr)):
            tmp = arr[i]
            j = i
            while j >= dist and tmp < arr[j - dist]:
                arr[j] = arr[j - dist]
                j -= dist
            arr[j] = tmp
        if dist == 1:
            break
    return arr


@calc_time
@jit(cache=True)
def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr
    step = 0
    while math.pow(2, step) < length:
        result = np.empty_like(arr)
        offset = 0
        left_start = offset
        pow_step = int(math.pow(2, step))
        left_end = pow_step + offset
        right_end = pow_step * 2 + offset
        while left_start < length:
            left, right = arr[left_start:left_end], arr[left_end:right_end]
            i = 0
            j = 0
            llen = len(left)
            rlen = len(right)
            while i < llen and j < rlen:
                if left[i] < right[j]:
                    result[left_start + i + j] = left[i]
                    i += 1
                else:
                    result[left_start + i + j] = right[j]
                    j += 1
            if i != llen:
                result[(left_start + i + j):right_end] = left[i:]
            elif j != rlen:
                result[(left_start + i + j):right_end] = right[j:]
            offset = right_end
            left_start = offset
            left_end = pow_step + offset
            right_end = pow_step * 2 + offset
        arr = result
        step += 1
    return arr


@calc_time
# @jit(cache=True)
def quick_sort(arr):
    qsort(arr, 0, len(arr))
    return arr


@jit(cache=True)
def qsort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        qsort(arr, low, pivot)
        qsort(arr, pivot + 1, high)


@jit(cache=True)
def partition(arr, low, high):
    p = arr[low]
    j = low
    for i in range(low + 1, high):
        if arr[i] < p:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[low], arr[j] = arr[j], arr[low]
    return j


@calc_time
def numpy_quick_sort(arr):
    arr.sort(kind='quicksort')
    return arr


@calc_time
def numpy_merge_sort(arr):
    arr.sort(kind='mergesort')
    return arr


@calc_time
def numpy_heap_sort(arr):
    arr.sort(kind='heapsort')
    return arr


if __name__ == '__main__':
    size = 1000000
    arr = (np.random.rand(size) * 100)  # m.astype(np.int)
    # arr.sort()
    algos = [
        # bubble_sort,
        # select_sort,
        # insert_sort,
        shell_sort,
        merge_sort,
        quick_sort,
        numpy_quick_sort,
        numpy_merge_sort,
        numpy_heap_sort
    ]
    # select_sort: 0.172759
    # insert_sort: 0.030061
    # bubble_sort: 0.117479
    # numpy_sort: 0.000417

    # len = 1000000
    # shell_sort: 0.198706
    # merge_sort: 0.109793
    # quick_sort: 0.087326
    # numpy_quick_sort: 0.059800
    # numpy_merge_sort: 0.071746
    # numpy_heap_sort: 0.106557
    for a in algos:
        a(arr)
