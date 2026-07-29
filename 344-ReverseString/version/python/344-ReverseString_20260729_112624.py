# Last updated: 7/29/2026, 11:26:24 AM
1class Solution(object):
2    def reverseString(self, s):
3        l=0
4        r=len(s)-1
5        while l<r:
6            s[l],s[r]=s[r],s[l]
7            l+=1
8            r-=1
9        return s
10                    