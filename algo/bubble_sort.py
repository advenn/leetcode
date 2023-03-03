import random

array = [random.randint(0, 100) for i in range(50)]
print(array)


def bubble_sort(array: list):
    """
    ikkitani tekshirish,
    condition bilan swap qilish,
    swaplar soni 0 ta bo'lsa to'xtatish
    """
    while True:
        swap_count = 0
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
                swap_count += 1
        if swap_count == 0:
            return array


array = bubble_sort(array)
print(array)
