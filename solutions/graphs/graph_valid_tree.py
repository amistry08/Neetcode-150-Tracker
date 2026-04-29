
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(edge, parent):
            
            if edge in visit:
                return False
            
            visit.add(edge)
            for i in adj[edge]:
                if i == parent:
                    continue
                if not dfs(i, edge): return False
            
            return True
            
        return dfs(0, -1) and n == len(visit)
