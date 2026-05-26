
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or
                (r, c) in visit or grid[r][c] == 0):
                return 0
            
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
            
        totalarea = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    totalarea = max(totalarea, dfs(i, j))

        return totalarea