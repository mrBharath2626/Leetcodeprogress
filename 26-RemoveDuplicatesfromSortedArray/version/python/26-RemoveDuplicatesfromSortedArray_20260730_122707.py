# Last updated: 7/30/2026, 12:27:07 PM
1class Solution:
2    def removeDuplicates(self, n: List[int]) -> int:
3     l=0
4     for r in range(1,len(n)):
5         if n[l]!=n[r]:
6            l+=1
7            n[l]=n[r]
8     return l+1