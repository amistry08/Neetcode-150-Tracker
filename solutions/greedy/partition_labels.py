
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        
        return res

        # My SOL
        # hashT = {}
        # res = []
        # for c in s:
        #     hashT[c] = 1 + hashT.get(c, 0) 
        
        # curr = set()
        # i = 0
        # j = 0
        # while i < len(s):
        #     j += 1
        #     curr.add(s[i])
        #     hashT[s[i]] -= 1
        #     if hashT[s[i]] == 0:
        #         curr.remove(s[i])
        #         if len(curr) == 0:
        #             res.append(j)
        #             j = 0
        #     i += 1
    
        # return res

