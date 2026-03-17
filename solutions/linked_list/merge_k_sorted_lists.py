# Definition for singly-linked list.
from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        heap = []
        for i in range(len(lists)):
            head = lists[i]
            if head:
                heapq.heappush(heap,(head.val, i))
            
        while heap:
            val, index = heapq.heappop(heap)
            node.next = lists[index]
            node = node.next
            lists[index] = lists[index].next
            head = lists[index]
            if head:
                heapq.heappush(heap,(head.val, index))

        return dummy.next