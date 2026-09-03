#encode and decode string

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "~" + s
            
        return res
# added this string since its a integer, but needs to be converted
            
    def decode(self, s: str) -> List[str]: #two pointer to find delimiters
        #['4@neet5@co@de']  --> ['neet', 'co@de']
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '~':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
        
