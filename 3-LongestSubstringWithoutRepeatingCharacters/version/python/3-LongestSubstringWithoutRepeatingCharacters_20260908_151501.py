# Last updated: 9/8/2026, 3:15:01 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = {}
4        l = 0
5        output = 0
6        for r in range(len(s)):
7            if s[r] not in seen:
8                output = max(output,r-l+1)
9            else:
10                if seen[s[r]] < l:
11                    output = max(output,r-l+1)
12                else:
13                    l = seen[s[r]] + 1
14            seen[s[r]] = r
15        return output