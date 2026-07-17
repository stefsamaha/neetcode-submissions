class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0

        # first, find meeting point inside cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
            if slow == fast:
                break 
        
        # second, find the entrance of the cycle 
        second = 0

        while slow != second:
            slow = nums[slow]
            second = nums[second]
        
        return slow
            
        
        