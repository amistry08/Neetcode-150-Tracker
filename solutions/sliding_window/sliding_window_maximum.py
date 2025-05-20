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

    # class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     output = []
    #     q = deque()  # index
    #     l = r = 0

    #     while r < len(nums):
    #         while q and nums[q[-1]] < nums[r]:
    #             q.pop()
    #         q.append(r)

    #         if l > q[0]:
    #             q.popleft()

    #         if (r + 1) >= k:
    #             output.append(nums[q[0]])
    #             l += 1
    #         r += 1

    #     return output   