class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        res = []
        subset = []
        digits_char = {
            '2': ('A', 'B', 'C'),
            '3': ('D', 'E', 'F'),
            '4': ('G', 'H', 'I'),
            '5': ('J', 'K', 'L'),
            '6': ('M', 'N', 'O'),
            '7': ('P', 'Q', 'R', 'S'),
            '8': ('T', 'U', 'V'),
            '9': ('W', 'X', 'Y', 'Z'),
        }

        def dfs(index):
            
            if index >= len(digits):
                temp = ""
                for i in subset:
                    temp += i
                res.append(temp.lower())
                return
            
            curr_digit = digits[index]
            for i in digits_char[curr_digit]:
                subset.append(i)
                dfs(index + 1)
                subset.pop()

        dfs(0)
        return(res)