from collections import defaultdict
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges  = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2 ))


        return t if len(visit) == n else -1


        # My original solution using DFS
        # time = {node: float("inf") for node in range(1, n + 1)}
        # adj = {i:[] for i in range(1, n+1)}
        # for u, v, t in times:
        #     adj[u].append((v, t))

        # def dfs(node, tim):
        #     if tim >= time[node]:
        #         return

        #     time[node] = tim
        #     for i, j in adj[node]:
        #         dfs(i, tim + j)
        

        # dfs(k,0)
        # res = max(time.values())
        # return res if res < float('inf') else -1
