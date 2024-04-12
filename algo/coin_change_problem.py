def sumCombinations(total, numbers):
    def add(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def sumCombinations(resultAcc, sumAcc, total, numbers):
        if not numbers or total < 0:
            return (0, resultAcc)
        elif total == 0:
            return (1, [sumAcc] + resultAcc)
        else:
            return add(
                sumCombinations(resultAcc, sumAcc, total, numbers[1:]),
                sumCombinations(
                    resultAcc, [numbers[0]] + sumAcc, total - numbers[0], numbers
                ),
            )

    return sumCombinations([], [], total, sorted(numbers, reverse=True))[1]


print("\n".join([str(x) for x in sumCombinations(15, [3, 9, 1, 3])]))
