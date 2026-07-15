# Last updated: 7/15/2026, 12:14:57 PM
1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        left, right = 0, len(nums)-1
4        while left < right:
5            mid = int((left + right)/2)
6            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
7                left = mid + 1
8            else:
9                right = mid
10        return nums[left] 