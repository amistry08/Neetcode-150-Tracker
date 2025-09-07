class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r: int, c: int, idx: int) -> bool:
            # idx is the index of the next char to match in `word`
            if idx == len(word):           # matched all chars
                return True
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] != word[idx]):
                return False

            visited.add((r, c))
            # explore all four directions
            if (dfs(r+1, c, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1)):
                return True
            visited.remove((r, c))
            return False

        # try using each cell as a starting point
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False