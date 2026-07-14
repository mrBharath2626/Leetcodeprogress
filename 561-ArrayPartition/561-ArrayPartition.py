# Last updated: 7/14/2026, 1:59:00 PM
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()

        ans = 0

        for i in range(0, len(nums), 2):
            ans += nums[i]

        return ans