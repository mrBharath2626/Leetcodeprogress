# Last updated: 7/30/2026, 2:06:37 PM
1class Solution:
2    def moveZeroes(self, n: List[int]) -> None:
3     l=0
4     for i in range(len(n)):
5        if n[i]!=0:
6            n[l],n[i]=n[i],n[l]
7            l+=1
8            
9
10        