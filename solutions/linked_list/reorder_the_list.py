# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #finding mid point of the list
        slow, fast = head, head.next # type: ignore
        while fast and fast.next:
            slow = slow.next# type: ignore
            fast = fast.next.next

        #reverse the second half of the list
        second = slow.next # type: ignore
        prev = slow.next = None # type: ignore
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge two half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
