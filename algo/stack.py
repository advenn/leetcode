def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(5))


def fact2(x):
    """
    implement factorial with while loop
    """
    result = 1
    while x > 1:
        result *= x
        x -= 1
    return result


print(fact2(5))


def trisum(n, csum):
    while True:  # Change recursion to a while loop
        if n == 0:
            return csum
        n, csum = n - 1, csum + n  # Update parameters instead of tail recursion


# print(trisum(9, 0))
