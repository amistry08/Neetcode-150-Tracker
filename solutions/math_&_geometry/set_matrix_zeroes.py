from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        #determine which rows, cols need to zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True 

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0


        # zeros = set()

        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] == 0:
        #             zeros.add((r, c))
        
        # for r, c in zeros:
        #     #top
        #     for i in range(c - 1, -1, -1):
        #         matrix[r][i] = 0
        #     #down
        #     for i in range(c + 1, len(matrix[0])):
        #         matrix[r][i] = 0
        #     #right
        #     for i in range(r + 1, len(matrix)):
        #         matrix[i][c] = 0
        #     #left
        #     for i in range(r - 1, -1, -1):
        #         matrix[i][c] = 0

