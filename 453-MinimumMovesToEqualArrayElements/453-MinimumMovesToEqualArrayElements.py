# Last updated: 7/14/2026, 1:59:02 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mini: int = nums[0]
        size: int = len(nums)

        for i in range(0, size):
            mini = min(nums[i], mini)

        moves: int = 0

        for i in range(0, size):
            moves += (nums[i]-mini)

        return moves