def fibonacci(n: int):
    """
    return list of Fibonacci numbers lower than n
    """
    a, b = 0, 1
    fibs = []
    count = 0

    while count <= n:
        a, b = b, a + b
        fibs.append(a)
        count += 1
    return fibs[-1]


print(fibonacci(5))
