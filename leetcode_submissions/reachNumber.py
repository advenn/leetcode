# class Solution:
#     def reachNumber(self, target: int) -> int:
#         # # Take the absolute value of target
#         # target = abs(target)
#         #
#         # # Initialize the sum and the current step
#         # curr_sum = 0
#         # step = 0
#         #
#         # # Keep adding integers starting from 1 until curr_sum >= target
#         # while curr_sum < target or (curr_sum - target) % 2 != 0:
#         #     print(curr_sum, target, step)
#         #     step += 1
#         #     curr_sum += step
#         #
#         # return step


class Solution3:
    def reachNumber(self, target: int) -> int:
        """
        You are standing at position 0 on an infinite number line. There is a destination at position target.

        You can make some number of moves numMoves so that:

        On each move, you can either go left or right.
        During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
        Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.



        Example 1:

        Input: target = 2
        Output: 3
        Explanation:
        On the 1st move, we step from 0 to 1 (1 step).
        On the 2nd move, we step from 1 to -1 (2 steps).
        On the 3rd move, we step from -1 to 2 (3 steps).
        Example 2:

        Input: target = 3
        Output: 2
        Explanation:
        On the 1st move, we step from 0 to 1 (1 step).
        On the 2nd move, we step from 1 to 3 (2 steps).
        """
        target = abs(target)
        step = 0
        curr_sum = 0
        while curr_sum != target:
            next_sum = curr_sum + step + 1
            print(
                f"{next_sum = }, {next_sum - target=}, {target - curr_sum=}, {step = }, {curr_sum=}, {target = }, {target - curr_sum=} "
            )
            if target < next_sum:
                if next_sum - target < target - curr_sum:
                    steps_to_reach = next_sum - target
                    if steps_to_reach == 1 and step != 1:
                        step += 1
                    else:
                        step += 2 * steps_to_reach
                elif next_sum - target >= target - curr_sum:
                    steps_to_reach = target - curr_sum
                    if steps_to_reach == 1 and target - curr_sum:
                        step += 1
                    else:
                        step += 2 * steps_to_reach
                return step
            step += 1
            curr_sum += step
        return step


# class Solution2:
#     def reachNumber(self, target: int) -> int:
#         # Take the absolute value of target
#         target = abs(target)
#
#         # Initialize the sum and the current step
#         curr_sum = 0
#         step = 0
#
#         # Keep adding integers starting from 1 until curr_sum >= target
#         while curr_sum < target or (curr_sum - target) % 2 != 0:
#             step += 1
#             curr_sum += step
#
#         return step

class Solution:
    def reachNumber(self, target: int) -> int:
        """

        """
        target = abs(target)
        current_sum = 0
        step = 0
        while current_sum <= target:
            if current_sum == target:
                return step
            step += 1
            current_sum += step
        delta = current_sum - target
        S = current_sum


if __name__ == "__main__":
    solution = Solution()
    # print(f"{solution.reachNumber(2) = }")  # Output: 3
    print(f"{solution.reachNumber(3) = }")  # Output: 2
    # print(f"{solution.reachNumber(8) = }")  # Output: 4
    # print(f"{solution.reachNumber(4) = }")  # Output: 3
    print(f"{solution.reachNumber(6) = }")  # Output: 3
