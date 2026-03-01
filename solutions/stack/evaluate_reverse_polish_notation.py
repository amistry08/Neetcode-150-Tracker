from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    res = b + a
                if i == "-":
                    res = b - a
                if i == "*":
                    res = b * a
                if i == "/":
                    res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(i))

        return stack[0]