class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""

        countT, window = {}, {} 

        for x in t:
            countT[x] = 1 + countT.get(x, 0) # build fixed dictionary for t 
        
        have, need = 0, len(countT)
        result, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c]==countT[c]:
                have +=1
                while have == need:
                    # update result 
                    if (r - l + 1) < resLen:
                        result = [l, r]
                        resLen = (r - l + 1)
                    # pop from left of window 
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        have -= 1
                    l+=1
        
        l, r = result 
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""





        
        