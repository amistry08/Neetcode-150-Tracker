class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
       
        p = {(x,y):[] for x, y in points}
        for x_i, y_i in points:
            for i in range(len(points)):
                    if([x_i, y_i] == points[i]):
                        continue
                    x_j, y_j = points[i]
                    p[(x_i,y_i)].append((abs(x_i - x_j) + abs(y_i - y_j), i))
            p[(x_i,y_i)] = sorted(p[(x_i,y_i)])

        total_cost = 0
        visited = set()
        x,y = points[0]
        minH = [[0,(x,y)]] #[cost, key]

        while len(visited) < len(points):
            cost, k = heapq.heappop(minH)
            if k in visited:
                continue
            total_cost += cost
            visited.add(k)
            for nei_cost, index in p[k]:
                x,y = points[index]
                heapq.heappush(minH, [nei_cost, (x,y)])
            
        return total_cost
            
# mininum spanning tree - prims algorithm
# O(N^2 log N) time | O(N^2) space