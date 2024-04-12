from typing import List

# n = 3  # Desired length
# binary_string = "0b0"  # Your binary string
#
# # Format the binary string to a fixed length with leading zeros
# formatted_string = format(int(binary_string, 2), f'0{n}b')
#
# print(formatted_string)  # Output: "000"


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        sample: ["111","011","001"]
        n = 3
        3 bit bilan maks 2^3 - 1 gacha ifodalash mumkin, bu misolda 0 dan 7 gacha sonlarni ifodalash mumkin
        algo:
        n bo'yicha maks sonni topish, 0 dan boshlab ungacha son yaratib uni tekshirish
        """
        length = len(nums[len(nums) - 1])
        max_num = (2**length) - 1
        print(max_num)
        for i in range(max_num):
            binary_string = bin(i)
            formatted_string = format(int(binary_string, 2), f"0{length}b")
            if formatted_string not in nums:
                return formatted_string
        return ""


s = Solution()
print(f"{s.findDifferentBinaryString(['0']) = }")
