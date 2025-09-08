# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = {}
        if not root:
            return []
        queue = deque([[root, 0]])
        
        while queue:
            node, currLevel = queue.popleft()
            res.setdefault(currLevel, []).append(node.val)

            if node.left:
                queue.append([node.left, currLevel+1])
            if node.right:
                queue.append([node.right, currLevel+1])
            
        return list(res.values())