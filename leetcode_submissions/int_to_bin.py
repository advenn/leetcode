import random
import time
from icecream import ic


class Solution:
    def toLowerCase(self, s: str) -> str:
        bytearray_data = bytearray(s, "ascii")
        for index, value in enumerate(bytearray_data):
            if 65 <= value <= 90:
                bytearray_data[index] = value + 32
        return bytearray_data.decode("ascii")

    def int2bin_num(self, num: int) -> str:
        n = num
        degree = 0
        while n >= 2:
            n //= 2
            degree += 1
        bin_degrees = [2**i for i in range(degree, -1, -1)]
        summ = 0
        nums = []
        length_bd = len(bin_degrees)
        while summ <= num:
            for index, bin_degree in enumerate(bin_degrees):
                if summ == num:
                    break
                if summ + bin_degree <= num:
                    summ += bin_degree
                    nums.append(length_bd - index - 1)

            break

        response = ["0"] * length_bd
        for i in nums:
            response[length_bd - i - 1] = "1"
        return "0b" + "".join(response)

    def int2bin_str(self, num: int) -> str:
        result = ""
        while num != 0:
            digit = num % 2
            result += str(digit)
            num //= 2
        return "0b" + result[::-1]


s = Solution()
nums = [random.randint(0, 100000) for _ in range(1000000)]
start = time.time()
for n in nums:
    s.int2bin_num(n)
ic(1, time.time() - start)


start = time.time()
for n in nums:
    s.int2bin_str(n)
ic(2, time.time() - start)
# n = "111111"
# ic(int(n, 2), bin(int(n, 2) >> 3), (int(n, 2) >> 3) & 1)
