class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        first_number = int(num1)
        length = len(num2)
        result = 0
        count = 0
        while True:
            result += first_number * (int(num2[-1 - count]) * (10**count))
            count += 1
            if count >= length:
                break
        return str(result)


s = Solution()
print(s.multiply("123", "456"))
print(s.multiply("2", "3"))
