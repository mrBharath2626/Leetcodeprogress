# Last updated: 7/29/2026, 3:54:27 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3      l=0
4      for i in range(len(nums)):
5        if nums[i]!=0:
6            if nums[l]!=nums[i]:
7             nums[l],nums[i]=nums[i],nums[l]
8            l+=1
9        
10            
11
12        