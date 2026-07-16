class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            val = abs(nums[i])
            index = val - 1

            if nums[index] < 0:
                return val 
            
            nums[index] = -nums[index]
        
        