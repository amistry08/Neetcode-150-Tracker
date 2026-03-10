# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next
            if slow == fast:
                return True     

        return False
    
'''Solution with Hash Set Space O(n) Time O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {}

        curr = head
        while curr:
            if curr in nodes:
                return True
            nodes[curr] = curr
            curr = curr.next 

        return False
'''