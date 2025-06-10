# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        
        return False

        # First Approach: Using a set to track visited nodes with O(n) space complexity
        # nodes = []
        # while head:
        #     nodes.append(head)
        #     print(nodes)
        #     if (head.next in nodes):
        #         return True
        #     head = head.next
        # return False