# Last updated: 7/14/2026, 1:59:17 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=[]
        for i in nums:
             if i not in temp:
                temp.append(i)
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp) 
            