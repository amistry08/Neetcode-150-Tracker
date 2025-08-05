class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
    
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res

        # res = []
        # subset = []
        # def dfs(curr_sum):
        #     if curr_sum > target:
        #         return []
        #     if curr_sum == target:
        #         res.append(subset.copy())
            
        #     for i in nums:
        #         subset.append(i)
        #         dfs(i+curr_sum)
        #         subset.pop()

        # def remove_duplicates(lst):
        #     seen = set()
        #     result = []

        #     for sublist in lst:
        #         key = tuple(sorted(sublist))
        #         if key not in seen:
        #             seen.add(key)
        #             result.append(sublist)
            
        #     return result

        # dfs(0)
        # return remove_duplicates(res)
    

    