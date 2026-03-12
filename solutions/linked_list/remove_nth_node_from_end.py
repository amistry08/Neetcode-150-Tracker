# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = head
        second = dummy

        while n > 0:
            first = first.next  # type: ignore
            n -= 1

        while first:
            first = first.next
            second = second.next  # type: ignore

        second.next = second.next.next # type: ignore
        return dummy.next

        