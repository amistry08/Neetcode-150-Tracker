# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self,root, maxVal):

        if not root:
            return 0

        res = 1 if root.val >= maxVal else 0
        maxVal = max(root.val, maxVal)
        res += self.dfs(root.left, maxVal)
        res += self.dfs(root.right, maxVal)
        return res