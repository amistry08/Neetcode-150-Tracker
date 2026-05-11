from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for s, d, p in flights:
            adj[s].append([d, p])
        
        visit = set()
        minH = [(0, src, 0)]
        res = -1

        while minH:
            price, node, pathlen = heapq.heappop(minH)

            if node == dst and pathlen <= k + 1:
                return price
            
            for d, p in adj[node]:
                heapq.heappush(minH, (p + price, d, pathlen + 1))
           
        return -1
