
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res
        
        
        # res = []
        
        # def dfs(i,cur):
        #     print(cur)
        #     if len(cur) == len(nums):
        #         res.append(cur.copy())

        #     for n in nums:
        #         if n in cur:
        #             continue
        #         cur.append(n)
        #         dfs(i+1, cur)
        #         cur.pop()

        # dfs(0, [])
        # return res
