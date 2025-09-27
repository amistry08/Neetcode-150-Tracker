class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n - 1):
            return False
        
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        path = set()
        maxPath = 0

        def dfs(node, prev):
            if node in path:
                return False

            path.add(node)
            for p in graph[node]:
                if p == prev:
                    continue
                if dfs(p, node) == False:
                    return False
            return True 

        return dfs(0,-1) and len(path) == n