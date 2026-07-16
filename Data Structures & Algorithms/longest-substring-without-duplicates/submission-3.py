class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {} # dictionary to keep track of the indeces seen | key: char, value: index
        l = 0   # left pointer initialized 
        length = 0  # length initialized 

        for r in range(len(s)): # right index starts at 0 and moves up 
            char = s[r]
            if char in seen:
                l = max(seen[s[r]]+1, l)
            seen[s[r]] = r
            
            length = max(length, r - l + 1)

        return length

        