class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                res.append(c)
            else:
                if res:
                    curr = res.pop()
                    if (curr == '[' and c == ']') or (curr == '{' and c == '}') or (curr == '(' and c == ')'):
                        continue
                return False
        return True if len(res) == 0 else False