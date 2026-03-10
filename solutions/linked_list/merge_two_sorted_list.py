# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Same Soluition but optimized code
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2

        dummy = res = ListNode()

        while one and two:
            if one.val <= two.val:
                res.next = one
                one = one.next
            else:
                res.next = two
                two = two.next
            res = res.next
                  
        res.next = one or two
        
        return dummy.next

''' Try One
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2

        res = ListNode()
        dummy = res

        while one and two:
            if one.val <= two.val:
                res.next = ListNode(one.val)
                one = one.next
            else:
                res.next = ListNode(two.val)
                two = two.next
            res = res.next
                  
        while one:
            res.next = ListNode(one.val)
            one = one.next
            res = res.next

        while two:
            res.next = ListNode(two.val)
            two = two.next
            res = res.next
        
        return dummy.next
'''