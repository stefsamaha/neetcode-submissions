class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            rob2, rob1 = 0, 0 

            for x in nums:
                temp = max(rob2 + x, rob1)
                rob2 = rob1 
                rob1 = temp 
            
            return rob1
        
        return max(helper(nums[1:]), helper(nums[:-1]))