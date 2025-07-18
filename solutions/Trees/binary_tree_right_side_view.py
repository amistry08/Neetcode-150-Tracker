# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = {}
        if not root:
            return []
        
        queue = deque([[root, 0]])
        while queue:
            node, level = queue.popleft()
            res.setdefault(level, []).append(node.val)

            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        
        result = []
        for k in res:
            result.append(res[k][-1])
            
        return result
        

