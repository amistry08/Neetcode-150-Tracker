from collections import deque
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = set()
        if amount == 0:
            return 0
        
        q = deque()
        q.append([amount, 0])
        while q:
            amt, count = q.popleft()
            if amt == 0:
                return count
            for i in coins:
                if amt - i in memo:
                    continue
                if i <= amt:
                    memo.add(amt - i)
                    q.append([amt - i, count + 1])
        return -1

'''
DP solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        print(dp)
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    print(a, dp)
        return dp[amount] if dp[amount] != amount + 1 else -1
'''
