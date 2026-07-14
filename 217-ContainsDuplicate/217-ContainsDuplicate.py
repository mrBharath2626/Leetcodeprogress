# Last updated: 7/14/2026, 1:59:06 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if i in s:
                return True
            s.add(i)

        return False
