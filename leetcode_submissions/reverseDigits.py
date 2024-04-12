from icecream import ic


class Solution:
    def reverseDigits(self, n: int):
        """
        n = 451 -> 154
        """
        num_rooms = []
        num = n
        while num >0:
            num, mod = divmod(num, 10)
            num_rooms.append(mod)
        num_length = len(num_rooms)
        rev_num = 0
        for index, num in enumerate(num_rooms):
            rev_num += num * 10 ** (num_length - 1 - index)
        ic(num_rooms, rev_num)
        return rev_num


s = Solution()
ic(s.reverseDigits(3))
