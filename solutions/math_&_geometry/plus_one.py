from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry, i = 1, 0

        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1

        digits.reverse()
        return digits 

        # My solution
        # num = ""
        # for n in digits:
        #     num += str(n)
        # num = 1 + int(num)
        # return [int(x) for x in str(num)]