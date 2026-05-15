from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(num):
            one, two = 0, 0
            for n in num:
                temp = max(one + n, two)
                one = two
                two = temp
            return two
        
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))