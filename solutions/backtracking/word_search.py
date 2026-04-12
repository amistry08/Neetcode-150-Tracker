
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def backtrack(i, j, index):
            if index == len(word):
                return True

            if i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] != word[index] or (i, j) in visited:
                return False
            
            visited.add((i,j))
            res =  backtrack(i + 1, j, index + 1 ) or backtrack(i, j + 1, index + 1) or backtrack(i - 1, j, index + 1) or backtrack(i, j- 1, index + 1)
            visited.remove((i,j))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if word[0] == board[i][j]:
                    if backtrack(i, j, 0):
                        return True

        return False 