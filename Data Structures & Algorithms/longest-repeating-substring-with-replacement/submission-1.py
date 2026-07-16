class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = 0
        l = 0
        counts = [0]*26

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while (r-l+1) - max(counts) > k: # still cant convert this whole window into one character using ≤ k replacements
                counts[ord(s[l]) - 65] -=1 # char at l is leaving the window so we update its count
                l += 1 # move the window 
            
            length = max(length, r-l+1)

        
        return length 
            



        