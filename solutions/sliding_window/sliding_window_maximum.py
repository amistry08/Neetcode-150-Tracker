from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []  # (-value, index)
        res = []
        l = 0

        for r, x in enumerate(nums):
            heapq.heappush(pq, (-x, r))

            if r - l + 1 == k:
                # remove stale indices
                while pq and pq[0][1] < l:
                    heapq.heappop(pq)

                res.append(-pq[0][0])
                l += 1

        return res