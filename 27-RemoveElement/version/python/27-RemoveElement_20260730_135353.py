# Last updated: 7/30/2026, 1:53:53 PM
1class Solution:
2    def removeElement(self, n: List[int], val: int) -> int:
3        l=0
4        for i in range(len(n)):
5            if n[i]!=val:
6                n[l]=n[i]
7                l+=1
8        return l
9
10