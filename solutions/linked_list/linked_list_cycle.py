class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       
        # Using HashSet  -> first approach     
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # lookup = {}

        # for n in nums:
        #     if(lookup.get(n)):
        #         return n
        #     lookup[n] = 1
        
        # Using Floyd's Tortoise and Hare (Cycle Detection)        
        # Time Complexity: O(n)
        # Space Complexity: O(1)            
        
        slow, fast = 0, 0
        
        # Find the intersection point in the cycle
        # The slow pointer moves one step at a time, while the fast pointer moves two steps
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the entrance to the cycle
        # Reset one pointer to the start and move both pointers one step at a time
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow



