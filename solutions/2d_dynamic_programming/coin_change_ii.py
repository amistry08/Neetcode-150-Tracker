from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)-1, -1, -1):
            nextDP = [0] * (amount+1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a-coins[i]]
            dp = nextDP
        return dp[amount]
        
        # res = []
        # count = 0
        
        # def dfs(amt, curSet):
        #     if amt == amount:
        #         if curSet not in res:
        #             nonlocal count 
        #             count += 1
        #             res.append(curSet.copy())
        #             return

        #     if amt > amount:
                
        #         return 

        #     for coin in coins:
        #         if coin in curSet:
        #             curSet[coin] += 1
        #         else:
        #             curSet[coin] = 1
        #         dfs(amt + coin, curSet)
        #         if curSet[coin] - 1 == 0:
        #             curSet.pop(coin)
        #         else:
        #             curSet[coin] -= 1 

        # dfs(0, {})
        # return count



