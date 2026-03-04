from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minVal = nums[0]
        
        if nums[l] < nums[r]:
            return nums[0]
                   
        while l <= r:
            m = (r+l) // 2
            minVal = min(minVal, nums[m])
            if nums[m] < nums[r]:
                if nums[m-1] < nums[m]:
                    r = m - 1
                else:
                    return nums[m]
            else:
                l = m + 1
                   
        return minVal
