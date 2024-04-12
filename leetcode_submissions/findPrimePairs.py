from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def sieve_of_eratosthenes(num: int, return_type="sum") -> int or list:
            primes = [True for _ in range(num + 1)]
            p = 2
            while p * p <= num:
                if primes[p]:
                    for i in range(p * p, num + 1, p):
                        primes[i] = False
                p += 1
            primes.pop(0)

            nums = []
            for index, val in enumerate(primes, 1):
                if val and index > 1:
                    nums += [index]
            return nums

        def binary_search(array, x, low, high):
            # Repeat until the pointers low and high meet each other
            while low <= high:
                mid = low + (high - low) // 2
                if array[mid] == x:
                    return mid
                elif array[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        primes = sieve_of_eratosthenes(n, return_type="nums")
        mid = n // 2 + 1
        response = []

        for i in primes:
            if i < mid:
                second = binary_search(primes, n - i, 0, len(primes) - 1)
                if second != -1:
                    if [min([i, n - i]), max([i, n - i])] not in response:
                        response.append([min([i, n - i]), max([i, n - i])])
        return response


s = Solution()
print(s.findPrimePairs(1000000))
