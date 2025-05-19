class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        array_max = []
        count = {}
        l = 0

        for r in range(len(nums)):
            c = nums[r]
            count[c] = 1 + count.get(c,0)
            if(r-l +1 == k):
                array_max.append(max(count.keys()))
                count[nums[l]] = count.get(nums[l]) - 1 
                if(count[nums[l]] == 0):
                    count.pop(nums[l])
                l += 1 
        
        return array_max
            