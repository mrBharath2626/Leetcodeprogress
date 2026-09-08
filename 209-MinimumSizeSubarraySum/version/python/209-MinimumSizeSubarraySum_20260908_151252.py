# Last updated: 9/8/2026, 3:12:52 PM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        n = len(nums)
4        left = 0 
5        total = 0 
6        min_len = 1e5+10
7        for right in range (n): 
8            total += nums[right]
9            while total >= target:
10                cur_len = right - left + 1 
11                total -= nums[left]
12                left += 1
13                min_len = min(cur_len, min_len)
14        if min_len == 1e5 + 10: 
15            return 0
16        return min_len
17