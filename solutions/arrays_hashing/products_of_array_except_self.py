class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preffix , suffix = [1]*len(nums),[1]*len(nums)
        prod = 1
        for i in range(1,len(nums)):
            prod *= nums[i-1]
            preffix[i] = prod
        prod = 1 
        for i in range(len(nums)-2, -1, -1):
            prod *= nums[i+1]
            suffix[i] = prod
        print(preffix, suffix)
        return [preffix[i]*suffix[i] for i in range(len(nums))]