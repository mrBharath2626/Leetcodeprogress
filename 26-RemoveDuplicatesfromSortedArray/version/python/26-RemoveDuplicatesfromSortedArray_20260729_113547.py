# Last updated: 7/29/2026, 11:35:47 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        temp=[]
4        for i in nums:
5             if i not in temp:
6                temp.append(i)
7        for i in range(len(temp)):
8            nums[i] = temp[i]
9        return len(temp) 
10            