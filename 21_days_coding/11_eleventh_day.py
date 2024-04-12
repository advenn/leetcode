class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        return len(str(num)) == len(str(num).strip("0"))
