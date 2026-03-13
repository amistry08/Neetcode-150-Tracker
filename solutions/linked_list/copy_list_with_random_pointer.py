
from typing import Optional



class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None): # type: ignore
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = Node(0)
        dummy = new
        start = head
        oldToNew = {}
        while start:
            dummy.next = Node(start.val)
            oldToNew[start] = dummy.next
            start = start.next
            dummy = dummy.next

        dummy = new.next
        while head:
            if head.random:
                dummy.random = oldToNew[head.random]
            else:
                dummy.random = None  # type: ignore
            dummy = dummy.next
            head = head.next

        return new.next