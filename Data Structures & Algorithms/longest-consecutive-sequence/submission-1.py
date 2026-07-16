class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums) #convert list to set 
        longest = 0

        for x in numSet:
            # check if x-1 exists or not 
            if (x-1) not in numSet:
                length = 1
                while (x + length) in numSet:
                    length += 1 
                
                longest = max(longest, length)
        
        return longest
                

