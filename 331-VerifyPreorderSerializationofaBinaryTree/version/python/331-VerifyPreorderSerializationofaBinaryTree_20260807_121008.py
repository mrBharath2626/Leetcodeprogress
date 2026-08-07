# Last updated: 8/7/2026, 12:10:08 PM
1class Solution:
2    def isValidSerialization(self, preorder: str) -> bool:
3        slots = 1
4        for i in preorder.split(','):
5            slots = slots-1
6            if slots < 0:
7                return False
8            if i != '#':
9                slots = slots+2
10        return slots == 0
11        