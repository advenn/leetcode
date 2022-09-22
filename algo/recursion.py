def countdown(i):
    print(i)
    if i <= 0:  # Base     case
        return
    else:  # Recursive    case
        countdown(i - 1)


# countdown(10)


def summ(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(summ([1, 2, 3, 4]))


def summ2(x: list):
    if not x:
        return 0
    return x[0] + summ2(x[1:])


print(summ2([1, 2, 3, 4]))
