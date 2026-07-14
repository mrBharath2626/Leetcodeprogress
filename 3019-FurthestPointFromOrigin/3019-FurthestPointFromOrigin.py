# Last updated: 7/14/2026, 1:58:35 PM
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        x, r=0, 0
        for c in moves:
            x+=(c=='R')-(c=='L')
            r+=c=='_'
        return abs(x)+r