# Last updated: 9/11/2026, 12:08:05 PM
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        l=r=0    
4        for r in range(len(nums)):
5            if nums[r] == 0:
6                k-=1
7            if k<0:
8                if nums[l] == 0:
9                    k+=1
10                l+=1
11        return r-l+1