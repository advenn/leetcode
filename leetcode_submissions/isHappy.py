# class Solution:
#     def isHappy(self, n: int) -> bool:
#         repeated = set()
#         while True:
#             nums = list(map(int, str(n)))
#             n = sum([x * x for x in nums])
#             if n == 1:
#                 return True
#             if n not in repeated:
#                 repeated.add(n)
#                 continue
#         return False
#
#     def isHappyOld(self, n: int) -> bool:
#         if n == 1:
#             return True
#         repeated = {}
#         while n > 0:
#             nums = []
#             while n > 0:
#                 nums.append(n % 10)
#                 n = n // 10
#             n = sum([x * x for x in nums])
#             if n not in repeated:
#                 return self.isHappyOld(n)
#             else:
#                 return False
#         return False
# def isHappy(self, n: int) -> bool:
#     nums = list(map(int, str(n)))
#     happened = {}
#     while True:
#         squared = sum([x * x for x in nums])
#         if squared not in happened and squared < 10 and squared == 1:
#             return True
#
#
#
#
#     return False


# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def get_next_number(num):
#             return sum(int(digit) ** 2 for digit in str(num))
#         slow = n
#         fast = get_next_number(n)

#         while fast != 1 and slow != fast:
#             slow = get_next_number(slow)
#             fast = get_next_number(get_next_number(fast))


#         return fast == 1
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Input: n = 19
        Output: true
        Explanation:
        1**2 + 9**2 = 82
        8**2 + 2**2 = 68
        6**2 + 8**2 = 100
        1**2 + 0**2 + 0**2 = 1
        """
        used = set()
        while True:
            nums = list(map(int, str(n)))
            n = sum([i**2 for i in nums])
            if n < 10 and n == 1:
                return True
            print(used, n)
            if n in used:
                return False
            used.add(n)


s = Solution()
print(s.isHappy(1_111_111))
# print(s.isHappy(19))
print(s.isHappy(7))
# print(s.isHappy(221))
