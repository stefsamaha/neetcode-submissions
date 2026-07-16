class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)
        count1 = [0]*26
        count2 = [0]*26

        if n1 > n2: return False 

        for i in range(n1):
            count1[ord(s1[i])-ord('a')]+=1
            count2[ord(s2[i])-ord('a')]+=1

        if count1 == count2: return True

        for i in range(n1, n2):
            count2[ord(s2[i]) - ord('a')] += 1 # add to window the character at i 
            count2[ord(s2[i-n1]) - ord('a')] -= 1 # lose the character at i-n1 

            if count1 == count2: # check at each step if matches  
                return True 
        

        return False 


# If s1 is longer than s2, a permutation is impossible → return False
# Count the frequency of each character in:

# s1 (count1)
# First window of s2 with length len(s1) (count2)


# If the two frequency arrays match → a permutation exists → return True
# Slide the window across s2:

# Add the new character entering the window
# Remove the character leaving the window
# Compare the frequency arrays at each step


# If any window matches → return True
# If no match is found after sliding → return False
           





        
        
        