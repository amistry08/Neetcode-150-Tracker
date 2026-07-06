class Solution:
    def isHappy(self, n: int) -> bool:
    
        def sum(num):
            res = 0
            num = str(num)
            for n in num:
                res += (int(n) * int(n))

            return res
        
        output = set()
        while n != 1:
            n = sum(n)
            if n not in output:
                output.add(n)
            else:
                return False

        return True
