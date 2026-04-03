from typing import List
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x in points:
            distance = self.euclideanDistance(x[0], x[1])
            heapq.heappush(heap,(distance, x))
        
        while k>0:
            d, x = heapq.heappop(heap)
            res.append(x)
            k -= 1

        return res

    def euclideanDistance(self,x1, x2):
        return math.sqrt(abs(x1)**2 + abs(x2)**2)