class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()
        visited_fresh = set()

        def nextGrid(r,c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visited or grid[r][c] == 0):
                return
            
            visited.add((r,c))
            visited_fresh.remove((r,c))
            q.append([r,c])
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visited.add((r,c))
                if grid[r][c] == 1:
                    visited_fresh.add((r,c))

        if len(visited_fresh) == 0:
            return 0

        minutes = -1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                nextGrid(r+1,c)
                nextGrid(r,c+1)
                nextGrid(r-1,c)
                nextGrid(r,c-1)

            minutes += 1
    
        if len(visited_fresh) > 0:
            return -1

        return minutes