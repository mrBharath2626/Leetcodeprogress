# Last updated: 7/29/2026, 3:42:15 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        for i in s:
4          if not i.isalnum() :
5            s = s.replace(i, "")
6        s = s.lower()
7
8        l = 0
9        r = len(s) - 1
10        f = True
11
12        while l < r:
13            if s[l] != s[r]:
14                f = False
15                break
16
17            l += 1
18            r -= 1
19
20        return f