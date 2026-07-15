# Last updated: 7/15/2026, 11:39:00 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        minheap = []
4        for i in nums:
5            heapq.heappush(minheap, i)
6            if len(minheap) > k:
7                heapq.heappop(minheap)
8        return minheap[0]