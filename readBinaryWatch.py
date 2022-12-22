from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = (1, 2, 4, 8)
        minutes = (1, 2, 4, 8, 16, 32)
        if turnedOn > 8:
            return []
        if turnedOn == 0:
            return ['00:00']

        def fill_minutes(minute: int):
            if type(min) == int and minute < 10:
                return f'0{minute}'




        return list('s')
