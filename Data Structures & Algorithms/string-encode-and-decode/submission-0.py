class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs)==0:
            return ""
        
        sizes = [len(x) for x in strs]
        result = ""

        for x in sizes:
            result += str(x)
            result += ","

        result += "#"

        for x in strs:
            result += x

        return result

# result     4,4,4,3#neetcodeloveyou
        
       
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes, result, i = [], [], 0

        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i+=1
            sizes.append(int(cur))
            i+=1 
        i+=1
        
        for x in sizes:
            result.append(s[i:i+x])
            i += x
        
        return result 
            
        