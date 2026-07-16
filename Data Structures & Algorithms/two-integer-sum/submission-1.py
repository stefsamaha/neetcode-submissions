class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}

        for i, x in enumerate(nums):
            need = target - x
            if need in sol:
                return [sol[need], i]
            sol[x]=i
            
         


        

        