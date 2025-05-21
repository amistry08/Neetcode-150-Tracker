class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if (i == "+" or i == "-" or i == "*" or i == "/"):
                a = s.pop()
                b = s.pop()
                s.append(int(eval(str(b) + i + str(a))))
            else:
                s.append(int(i))
        return s.pop()