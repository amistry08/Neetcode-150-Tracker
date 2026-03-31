# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        res = str()

        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res += str(node.val) + ','
            else:
                res += "#,"

        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
         
        data = data.split(",") #type: ignore
        print(data)
        if data[0] != "#" and data[0] != '':
            root = TreeNode(int(data[0]))
        else:
            return None

        q = deque()
        q.append(root)
        
        i = 1
        while i < len(data)-1:
            node = q.popleft()
            if data[i] == "#":
                node.left = None
            else:
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            
            i+= 1

            if data[i] == "#":
                node.right = None
            else:
                node.right = TreeNode(int(data[i]))
                q.append(node.right)

            i+=1
                
        return root
        
