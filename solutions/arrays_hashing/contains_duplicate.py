class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict={}
        for i in nums:
            if myDict.get(i) != None:
                return True
            else:
                myDict[i] = i
        return False    