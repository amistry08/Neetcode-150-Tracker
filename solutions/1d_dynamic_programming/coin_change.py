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