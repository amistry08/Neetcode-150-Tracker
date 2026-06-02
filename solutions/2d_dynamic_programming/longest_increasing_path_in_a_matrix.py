from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = {}
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


        def dfs(i, j, prev):

            if i < 0 or j < 0 or i >= m or  j >= n or matrix[i][j] <= prev:
                return 0

            if (i,j) in dp:
                return dp[(i, j)]
            
            res = 1
            for dr, dc in DIRECTIONS:
                res = max(res, 1 + dfs(i + dr, j + dc, matrix[i][j]))
            dp[(i, j)] = res

            return res 
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)
          
        return max(dp.values())