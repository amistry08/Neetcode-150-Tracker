class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def divide(l,r)-> int:
            if l > r:
                return -1
            m = l + (r-l) // 2
           
            if (nums[m] == target):
                return m
            if(nums[m] > target):
                return divide(l, m-1)
            if(nums[m] < target):
                return divide(m+1,r)
            
            return(l,m-1)

        return divide(0, len(nums)-1)