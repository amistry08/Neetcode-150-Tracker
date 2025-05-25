class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        def bs(l,r,i):

            if l > r:
                return -1

            m = l + (r-l) // 2

            if matrix[i][m] == target:
                return m
            if matrix[i][m] > target:
                return bs (l, m-1,i)
            if matrix[i][m] < target:
                return bs(m+1,r,i)
          
            return bs(l, m-1,i)
        
        res = -1

        for i in range(len(matrix)):
            n = len( matrix[i]) -1
            if target >= matrix[i][0] and target <= matrix[i][n]:
                res = bs(0,n, i)
        
        return True if res != -1 else False
       
        