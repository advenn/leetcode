from icecream import ic


def is_prime(n: int) -> bool:
    """
    implement sieve of eratosthenes
    """
    if n < 2:
        return False
    is_primes = [False, False] + [True for _ in range(n- 1)]
    for index in range(2, int(n**0.5) + 1):
        if is_primes[index]:
            for j in range(index, n, index):
                is_primes[j] = False

    ic(n, is_primes)
    return is_primes[-1]


for n in range(30):
    print(n, is_prime(n))
