# Last updated: 7/28/2026, 11:47:34 AM
1class Solution(object):
2    def maxArea(self, h):
3      ans=0
4      l=0
5      r=len(h)-1
6      while l<r:
7        a=(r-l)*min(h[r],h[l])
8        ans=max(ans,a)
9        if h[l]<h[r]:
10         l+=1
11        else:
12         r-=1
13      return ans