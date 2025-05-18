class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n={}
        m={}
        for i in s:
            if i in n:
                value = n.get(i)
                n.update({i:value+1})
            else:
                n.update({i:1})
        for i in t:
            if i in m:
                value = m.get(i)
                m.update({i:value+1})
            else:
                m.update({i:1})
        return(True if n==m else False)