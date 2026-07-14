# Last updated: 7/14/2026, 1:58:25 PM
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n - 1, -1, -1):
            nums.append(nums[i])

        return nums