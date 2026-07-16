class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i, n in enumerate(nums):
            d[n]=i
        
        for i, n in enumerate(nums):
            need = target - n 
            if need in d and d[need] != i:
                return [i, d[need]]
            
         


        

        