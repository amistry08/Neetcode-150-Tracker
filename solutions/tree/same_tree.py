# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(p, q):
            if not p and not q:    
                return
            
            if not p or not q or p.val != q.val:
                self.res = False
                return 

            dfs(p.left, q.left)
            dfs(p.right, q.right)

            return 

        dfs(p, q)
        return self.res