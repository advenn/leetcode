# leetcode link: https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        logic:
        array bo'ylab loop qilish,

        birinchi keys:
            sample list: [4,2,0,3,2,5]
            start ni olish, birinchi etapda 4
            undan keyingisi bilan tekshirish:
            4 < 2 => False
            keyingisiga o'tkazish.
            4 < 0 => False
            keyingisiga o'tkazish.
            4 < 3 => False
            keyingisiga o'tkazish.
            4 < 2 => False
            keyingisiga o'tkazish.
            4 < 5 => True

            maximumni aniqlash.

        ikkinchi keys:
            sample list: [0,1,0,2,1,0,1,3,2,1,2,1]



        uchinchi keys:
            sample list: [4,2,0,3,2]
            start ni olish, birinchi etapda 4
            undan keyingisi bilan tekshirish:
            4 < 2 => False
            keyingisiga o'tkazish.
            4 < 0 => False
            keyingisiga o'tkazish.
            4 < 3 => False
            keyingisiga o'tkazish.
            4 < 2 => False
            keyingisiga o'tkazish.

        """

        pass
