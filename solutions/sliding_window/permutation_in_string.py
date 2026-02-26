class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1, count_s2 = {}, {}

        for c in s1:
            count_s1[c] = 1 + count_s1.get(c,0)
        
        
        l = 0
        for r in range(len(s2)):
            count_s2[s2[r]] = 1 + count_s2.get(s2[r],0)
            if (r-l+1) != len(s1):
                continue
            else:
                if count_s1 != count_s2:
                    count_s2[s2[l]] -= 1
                    if (count_s2[s2[l]] == 0):
                        count_s2.pop(s2[l], None)
                    l += 1
            if count_s1 == count_s2:
                return True
        return False 
