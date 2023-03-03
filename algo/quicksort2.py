import random
import bubble_sort
nums = [random.randint(0, 1000) for i in range(100 // 2)]
print(len(nums), nums)


def quicksort(arr: list) -> list:
    """
    logic:
    array dan  pivot, undan kichiklar, va undan kattalarni alohida olib rekursiya bilan sort qilish
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


nums = quicksort(nums)
print(len(nums), nums)

print(quicksort(nums) == bubble_sort.bubble_sort(nums))
