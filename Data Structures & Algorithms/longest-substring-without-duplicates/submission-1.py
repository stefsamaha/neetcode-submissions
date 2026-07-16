class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {} # dictionary to keep track of the indeces seen | key: char, value: index
        l = 0   # left pointer initialized 
        length = 0  # length initialized 

        for r in range(len(s)): # right index starts at 0 and moves up 
            char = s[r]
            if char in seen and seen[char] >= l: # seen that char before and its last known position is >= l
                l = seen[char] + 1 
            else:
                length = max(length, r - l + 1)
                
            seen[char] = r # first time seen or updated index 
            

        return length 



        