class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
        three cases:
            1. rects cross, one of four points lies inside another
            2. rects don't cross
            3. one lies in another
        """
        ax11, ay11 = ax1, ay2
        ax12, ay12 = ax2, ay1

        bx11, by11 = bx1, by2
        bx12, by12 = bx2, by1

        result = 0
        # cross:
        


        return result