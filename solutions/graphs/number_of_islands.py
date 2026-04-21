from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROW, COL = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if (i < 0 or j < 0 or 
                i >=  ROW or j >= COL or
                (i, j) in visit or grid[i][j] == "0"):
                return 0

            visit.add((i, j))
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for x,y in directions:
                dfs(i+x, j+y)
            
            return 1

        for i in range(ROW):
            for j in range(COL):
                count += dfs(i, j)

        return count