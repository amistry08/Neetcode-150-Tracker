import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        
        
        
        # hand.sort()
        # n = len(hand) / groupSize

        # if len(hand) % groupSize > 0:
        #     return False

        # while n > 0:
        #     curr = hand[0]
        #     for i in range(groupSize):
        #         if curr in hand:
        #             hand.remove(curr)
        #             curr += 1
        #         else:
        #             return False
        #     n -= 1
        
        # return True
        
