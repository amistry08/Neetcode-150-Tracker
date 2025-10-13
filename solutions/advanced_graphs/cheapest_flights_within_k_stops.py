class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = {i:[] for i in range(n)}
        for fr, to, price in flights:
            adj[fr].append([to, price])

        self.minCost = -1
        visited = set()

        def dfs(fr, k_temp, cost):
            print(fr, k_temp, cost)
            
            if fr == dst:
                if self.minCost == -1:
                    self.minCost = cost
                else:
                    self.minCost = min(cost, self.minCost)
                return True

            if ((self.minCost > 0 and self.minCost < cost) or
                (k_temp == -1 and fr != dst) or
                (fr in visited)):
                return False

            for i_to, i_price in adj[fr]:
                visited.add(fr)
                dfs(i_to, k_temp-1, i_price + cost)
                visited.remove(fr)
            return True

        dfs(src, k, 0)
        return self.minCost


# Bellmen Ford Soltion
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         prices = [float("inf")] * n
#         prices[src] = 0

#         for i in range(k + 1):
#             tmpPrices = prices.copy()

#             for s, d, p in flights:  # s=source, d=dest, p=price
#                 if prices[s] == float("inf"):
#                     continue
#                 if prices[s] + p < tmpPrices[d]:
#                     tmpPrices[d] = prices[s] + p
#             prices = tmpPrices
#         return -1 if prices[dst] == float("inf") else prices[dst]