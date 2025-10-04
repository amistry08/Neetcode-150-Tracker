class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1


# dfs      
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         adj = defaultdict(list)
#         for u, v, w in times:
#             adj[u].append((v, w))

#         dist = {node: float("inf") for node in range(1, n + 1)}

#         def dfs(node, time):
#             if time >= dist[node]:
#                 return

#             dist[node] = time
#             for nei, w in adj[node]:
#                 dfs(nei, time + w)

#         dfs(k, 0)
#         res = max(dist.values())
#         return res if res < float('inf') else -1


# bfs
# class Solution:
#     def networkDelayTime(self, times, n, k):
#         adj = defaultdict(list)
#         for u, v, w in times:
#             adj[u].append((v, w))

#         dist = {node: float("inf") for node in range(1, n + 1)}
#         q = deque([(k, 0)])
#         dist[k] = 0

#         while q:
#             node, time = q.popleft()
#             if dist[node] < time:
#                 continue
#             for nei, w in adj[node]:
#                 if time + w < dist[nei]:
#                     dist[nei] = time + w
#                     q.append((nei, time + w))

#         res = max(dist.values())
#         return res if res < float('inf') else -1