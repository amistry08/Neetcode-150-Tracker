class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l  = 0
        check = {}
        count = {}
        
        for i in range(len(s1)):
            check[s1[i]] = 1 + check.get(s1[i],0)

        for i in range(len(s2)):
            count[s2[i]] = 1 + count.get(s2[i],0)
            if(i-l != len(s1) -1):
                continue
            else:
                if(count.items() == check.items()):
                    return True
                else:
                    count[s2[l]] = count.get(s2[l]) - 1
                    if(count[s2[l]] == 0):
                        count.pop(s2[l])
                l += 1

        return False
            
        print(count)