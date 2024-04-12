import typing


def check_prime(num: int) -> bool:
    if num < 2:
        return True
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    is_prime = True
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            is_prime = False
            return is_prime

    return is_prime


def sieve_of_eratosthenes(
    num: int, return_type: typing.Literal["sum", "count", "nums"] = "sum"
) -> int or list:
    primes = [True for _ in range(num + 1)]
    p = 2
    while p * p <= num:
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1
    primes.pop(0)
    if return_type == "sum":
        summ = 0
        for index, val in enumerate(primes, 1):
            if val:
                summ += index
        return summ
    elif return_type == "count":
        return sum(primes)
    elif return_type == "nums":
        nums = []
        for index, val in enumerate(primes, 1):
            if val and index > 1:
                nums += [index]
        return nums


print(sieve_of_eratosthenes(10, return_type="nums"))
