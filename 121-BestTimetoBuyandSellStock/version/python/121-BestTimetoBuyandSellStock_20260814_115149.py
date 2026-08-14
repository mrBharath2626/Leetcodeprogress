# Last updated: 8/14/2026, 11:51:49 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        max_profit=0
4        buy=prices[0]
5        for price in prices:
6            buy=min(buy,price)
7            max_profit=max(max_profit,price-buy)
8        return max_profit
9        