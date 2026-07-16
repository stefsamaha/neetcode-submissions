class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums) #convert list to set, removes duplicates and gives O(1) average-time membership checks
        longest = 0

        for x in numSet:
            # check if x-1 exists or not 
            if (x-1) not in numSet:
                length = 1
                while (x + length) in numSet:
                    length += 1 # length becomes the size of that consecutive run
                
                longest = max(longest, length) # update the max length 
        
        return longest
                

