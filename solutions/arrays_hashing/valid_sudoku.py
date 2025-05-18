class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash, colHash, sqHash = {},{},{}
        for i in range(0,9):
            colHash = {}
            rowHash = {}
            for j in range(0,9):
                n = board[i][j]
                m = board[j][i]


                #for checking Rows
                rowHash[n] = 1 + rowHash.get(n,0)
                for x,k in rowHash.items():
                    if(k>1 and x!="."): return False
                
                

                #for checking Columns
                colHash[m] = 1 + colHash.get(m,0)
                for x,k in colHash.items():
                    if(k>1 and x!="."): return False

                
                #for checking squares
                y = ((i//3) * 3)+(j//3)
                sqHash[y] = sqHash.get(y,{})
                sqHash[y][n] = sqHash[y].get(n,0) + 1
                for x,k in sqHash[(i//3)+(j//3)].items():
                    if(k>1 and x!="."): return False
                    
        return True
    
        
        
