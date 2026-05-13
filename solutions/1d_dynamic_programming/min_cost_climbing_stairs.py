from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1],cost[i+2])

        return min(cost[0], cost[1])
        
        
        # one, two = cost[0], cost[1]

        # for i in range(2, len(cost)):
        #     temp = two
        #     two = min(one, two) + cost[i]
        #     one = temp

        # return min(one, two)