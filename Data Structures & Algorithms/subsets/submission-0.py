class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for x in nums:
                res+= [sub + [x] for sub in res]
        
        return res

        