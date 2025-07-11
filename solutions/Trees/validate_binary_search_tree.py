# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.dfs(root, float('-inf'), float('inf'))


    def dfs(self, root, minVal, maxVal):
        if not root:
            return True

        if(minVal < root.val and root.val < maxVal):
            return self.dfs(root.left, minVal, root.val) and self.dfs(root.right, root.val, maxVal)
        else:
            return False
        