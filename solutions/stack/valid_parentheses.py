class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if(i == '(' or i == "{" or i == "["):
                res.append(i)
            else:
                if(len(res) > 0):
                    if( (i == "]" and res[-1] == "[") or (i == "}" and res[-1] == "{") or (i == ")" and res[-1] == "(")):
                        res.pop()
                        continue
                    else:
                        return False
                else:
                    return False
        return True if len(res) == 0 else False
                    
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

#         for c in s:
#             if c in closeToOpen:
#                 if stack and stack[-1] == closeToOpen[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
        
#         return True if not stack else False
