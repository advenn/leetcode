from icecream import ic


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Leetcode recommends to use Sieve of Eratosthenes
        2 dan n/2 gacha loop,
        """

        if n < 2:
            return 0
        is_prime = [False, False] + [True for _ in range(n - 1)]
        for index in range(2, int(n**0.5) + 1):
            if is_prime[index]:
                for j in range(index * index, n, index):
                    is_prime[j] = False

        return sum(is_prime)

        # prime_numbers = set()
        # complex_numbers = set()
        # initial_primes = (2, 3, 5)
        # for i in range(2, n):
        #     if i in initial_primes:
        #         prime_numbers.add(i)
        #         x = n // i
        #         for j in range(2, x ):
        #             complex_numbers.add(i * j)
        #             continue
        #     if i not in prime_numbers and i not in complex_numbers:
        #         prime_numbers.add(i)
        # ic(prime_numbers, complex_numbers)
        # return len(complex_numbers)


s = Solution()
print(s.countPrimes(10))
