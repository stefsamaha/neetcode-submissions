class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] in d:
                return True
            else:
                d[nums[i]]=1
        
        return False 

        
        