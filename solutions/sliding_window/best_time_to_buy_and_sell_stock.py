from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        if len(prices) < 2:
            return 0

        i, j = 0, 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i += 1
                j = i + 1
            else:
                profit = max(profit, prices[j]-prices[i])
                j += 1

        return profit