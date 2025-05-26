class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[l]

        if nums[l] <  nums[r]:
            return res
        
        while l<=r:
            m = r+l // 2
            res=min(res, nums[m])
            if nums[m] > nums[r]:
                l = m+1  
            else:
                r = m-1

        return res 