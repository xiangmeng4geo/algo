from time import time

import numpy as np
from numba import jit, cuda

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
# @jit(cache=True)
def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr
    step = 0
    while np.math.pow(2, step) < length:
        # left_start = 0
        # left_end = step ** 2
        # right_start = step ** 2
        # right_end = step ** 2
        print(step)
        step += 1
    return arr


@calc_time
def numpy_sort(arr):
    arr.sort()
    return arr


if __name__ == '__main__':
    size = 10000
    arr = (np.random.rand(size) * 100)  # m.astype(np.int)
    # arr.sort()
    algos = [
        bubble_sort,
        select_sort,
        insert_sort,
        shell_sort,
        merge_sort,
        numpy_sort
    ]
    # select_sort: 0.172759
    # insert_sort: 0.030061
    # bubble_sort: 0.117479
    # numpy_sort: 0.000417
    for a in algos:
        a(arr)
