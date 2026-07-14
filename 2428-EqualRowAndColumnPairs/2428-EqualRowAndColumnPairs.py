# Last updated: 7/14/2026, 1:58:42 PM
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        c=0
        for i in range(n):
            for j in range(n):
                row=grid[i]
                col=[]
                for k in range(n):
                  col.append(grid[k][j])
                if row==col:
                    c+=1
        return c