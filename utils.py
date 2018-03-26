from time import time

from numba import jit


@jit
def check_sort(arr):
    for i in range(0, len(arr) - 1):
        assert arr[i] <= arr[i + 1]


def calc_time(func):
    def time_it(in_arrs):
        arr = in_arrs.copy()
        start_time = time()
        out_arrs = func(arr)
        end_time = time()
        print("%s: %f" % (func.__name__, (end_time - start_time)))
        # print(out_arrs)
        check_sort(out_arrs)

    return time_it
