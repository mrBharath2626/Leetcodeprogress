# Last updated: 7/15/2026, 5:58:52 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4     l=0
5     r=len(nums)-1
6     while l<r:
7        s=nums[l] + nums[r]
8        if s == target:
9            return [l+1,r+1] 
10        elif s<target:
11            l+=1
12        else:
13            r-=1             
14         