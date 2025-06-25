# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            #reverse
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next


    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr
    
    
    #     count = 0
    #     while(count < k):
    #         curr = head
    #         while(count<k and head):
    #             head = head.next
    #             count += 1
    #         self.reverse(curr)
    #         if(k == count and head):
    #             count = 0
    #         else:
    #             count = k
    #     return head
       
    # def reverse(self, curr):
    #     prev, curr1 = None, head
    #     while(head):
    #         temp = curr1.next
    #         curr1.next = prev
    #         prev = head
    #         curr1 = temp
