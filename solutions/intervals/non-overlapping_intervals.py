from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res
        
        
        # intervals.sort()
        # res = [intervals[0]]
        # count = 0

        # print(intervals)
        # for i in range(1, len(intervals)):
        #     curMax = res[-1][1]
        #     if (intervals[i][0] < curMax):
        #         count += 1
        #         continue
        #     else:
        #         res.append(intervals[i])

        # return count
        
            
