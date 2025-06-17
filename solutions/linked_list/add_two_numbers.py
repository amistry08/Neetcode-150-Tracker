# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(0)
      
        while l1 and l2:
        
            add = l1.val + l2.val + node.val
            print(add)
            node.val = add%10
        
            l1 = l1.next
            l2 = l2.next 

            if(add>9):
                node.next = ListNode(1)
            elif (l1 or l2):
                node.next = ListNode(0)
            
            node = node.next

        while l1 or l2:
            add = 0
            if(l1):
                add = node.val + l1.val 
                node.val = add % 10
                l1 = l1.next
            if(l2):
                add = node.val + l2.val 
                node.val = add % 10
                l2 = l2.next

            if(add>9):
                node.next = ListNode(1)
            elif(l1 or l2):
                node.next = ListNode(0)

            node = node.next            


        return dummy