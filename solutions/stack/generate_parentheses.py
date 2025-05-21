class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN<n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # after backtracking complete we need to empty the stack
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack(0,0)

        return res

# only add open parenthesis if open < n
# only add close parenthesis if close < open
# if close == open == n