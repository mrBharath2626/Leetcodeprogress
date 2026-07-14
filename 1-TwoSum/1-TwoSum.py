# Last updated: 7/14/2026, 1:59:21 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i in range(len(nums)):
          d=target-nums[i]
          if d in mp:
             return[mp[d],i]
          mp[nums[i]] = i