class Solution:
    def longestPalindrome(self, s: str) -> str:
        index = 0 
        bestLen = 0 

        for i in range(len(s)):
            # odd length, starting index is the same
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > bestLen:
                    bestLen = r - l + 1
                    index = l 
                
                l -= 1
                r += 1

            # even length, starting indeces must differ 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > bestLen:
                    bestLen = r - l + 1
                    index = l 
                
                l -= 1
                r += 1

        return s[index : index + bestLen]               

