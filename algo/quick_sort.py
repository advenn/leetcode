import random
import time

import names


def quicksort(array):
    # print(array)
    if len(array) < 2:
        return array  # Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = random.choice(array)  # Recursive case
        less = [
            i for i in array[1:] if i <= pivot
        ]  # Sub-array of all the elements less than the pivot
        greater = [
            i for i in array[1:] if i > pivot
        ]  # Sub-array of all the elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)


def find_smallest(arr):
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


nums = [random.randint(1, 1000000) for i in range(10000)]
# name_lst = [names.get_first_name() for _ in range(1000)]

start = time.time()
(quicksort(nums))
print(time.time() - start)
start = time.time()
(selection_sort(nums))
print(time.time() - start)
