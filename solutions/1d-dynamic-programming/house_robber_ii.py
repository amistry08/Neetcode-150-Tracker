class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0

        for n in nums[:-1]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        max_rob = rob2

        rob1, rob2 = 0,0
        for n in nums[1:]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        if len(nums) == 1: return nums[0]
        return(max(max_rob, rob2))