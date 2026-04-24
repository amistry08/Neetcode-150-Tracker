from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def rotten(r, c):
            if (r < 0 or c < 0 or r>= ROW or c >= COL or
                (r, c) in visit or grid[r][c] != 1):
                return 

            visit.add((r, c))
            q.append((r, c))
            grid[r][c] = 2

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))

        minutes = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                rotten(r + 1, c)
                rotten(r, c + 1)
                rotten(r - 1 , c)
                rotten(r, c - 1)
        
            minutes += 1       
                
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1
        
        return minutes if minutes > -1 else  0


