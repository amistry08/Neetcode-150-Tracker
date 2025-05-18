class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(text)
        i = 0
        while (i<len(text)):
            if(text[i] != text[len(text)-1-i]):
                return False
            i +=1
        return True