# Last updated: 7/14/2026, 1:58:29 PM
class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        from collections import Counter

        # ---------- Horizontal ----------
        top_sum = 0
        top = Counter()
        bottom = Counter()

        for row in grid:
            bottom.update(row)

        for i in range(m - 1):
            for val in grid[i]:
                top_sum += val
                top[val] += 1
                bottom[val] -= 1
                if bottom[val] == 0:
                    del bottom[val]

            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            # TOP BIGGER
            if top_sum > bottom_sum:
                if self.valid_horizontal(grid, 0, i, n, diff, top):
                    return True
            else:
                if self.valid_horizontal(grid, i+1, m-1, n, diff, bottom):
                    return True

        # ---------- Vertical ----------
        left_sum = 0
        left = Counter()
        right = Counter()

        for row in grid:
            right.update(row)

        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                left_sum += val
                left[val] += 1
                right[val] -= 1
                if right[val] == 0:
                    del right[val]

            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                if self.valid_vertical(grid, 0, j, m, diff, left):
                    return True
            else:
                if self.valid_vertical(grid, j+1, n-1, m, diff, right):
                    return True

        return False

    # ---------- NO COPYING ----------
    def valid_horizontal(self, grid, r1, r2, n, diff, counter):
        if diff not in counter:
            return False

        rows = r2 - r1 + 1

        # 2D safe
        if rows > 1 and n > 1:
            return True

        # single row
        if rows == 1:
            return grid[r1][0] == diff or grid[r1][n-1] == diff

        # single column
        if n == 1:
            return grid[r1][0] == diff or grid[r2][0] == diff

        return False

    def valid_vertical(self, grid, c1, c2, m, diff, counter):
        if diff not in counter:
            return False

        cols = c2 - c1 + 1

        # 2D safe
        if m > 1 and cols > 1:
            return True

        # single column
        if cols == 1:
            return grid[0][c1] == diff or grid[m-1][c1] == diff

        # single row
        if m == 1:
            return grid[0][c1] == diff or grid[0][c2] == diff

        return False