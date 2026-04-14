from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2": ["a", "b", "c" ],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y","z"],
        }

        res = []
        subset = []

        if digits == "":
            return res

        def dfs(num):
            if len(digits) == len(subset):
                res.append("".join(subset))
                return
            
            for val in hashmap[digits[num]]:
                subset.append(val)
                dfs(num + 1)
                subset.pop()
            
        dfs(0)
        return res