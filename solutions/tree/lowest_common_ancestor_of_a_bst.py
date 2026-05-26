# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = p
        
        def dfs(root, p, q):
            if not root:
                return 

            if p == root.val or q == root.val:
                self.res = root
                return

            if p.val < root.val and q.val < root.val:
                dfs(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                dfs(root.right, p, q)
            else:
                self.res = root
                return 
                
        dfs(root, p, q)
        return self.res
            
        


