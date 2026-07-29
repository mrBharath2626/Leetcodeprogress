# Last updated: 7/29/2026, 12:11:06 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if len(nums) == 0:
4            return 0
5        l=0
6        for i in range(1,len(nums)):
7            if nums[l]!=nums[i]:
8                l+=1
9                nums[l]=nums[i]
10        return l+1
11        