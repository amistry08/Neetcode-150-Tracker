class Solution:

    def encode(self, strs: List[str]) -> str:
        en = "".join([f"{len(s)}|{s}"for s in strs])
        return en

    def decode(self, s: str) -> List[str]:
        i = 0
        dec = []
        while (i < len(s)):
            j = s.find('|', i)
            length = int(s[i:j])
            i = j+1

            word =   s[i:i+length]
            dec.append(word)    
            i += length
        return dec