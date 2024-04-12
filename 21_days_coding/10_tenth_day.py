class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        reversed_binary = binary[::-1]
        if len(reversed_binary) < 32:
            reversed_binary += "0" * (32 - len(reversed_binary))
        return int(reversed_binary, 2)


s = Solution()
print(s.reverseBits(n=43261596))
# print(s.reverseBits(n = ))
