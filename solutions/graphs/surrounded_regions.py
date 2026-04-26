from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        visit = set()
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROW or c == COL or 
                board[r][c] == 'X' or (r, c) in visit):
                return 
            
            board[r][c] = '#'
            visit.add((r, c))
            for rd, cd in directions:
                dfs(r + rd, c + cd)

        for r in range(ROW):
            for c in range(COL):
                if ((r < 1 or c < 1 or r == ROW - 1 or c == COL - 1) and 
                    board[r][c] == 'O'):
                    dfs(r, c)
                
        print(board)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == '#':
                    board[r][c] = 'O' 
                elif board[r][c] == 'O':
                    board[r][c] = 'X'