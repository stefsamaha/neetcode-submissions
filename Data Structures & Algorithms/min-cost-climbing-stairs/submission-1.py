class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def helper(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(helper(i + 1), helper(i + 2))
            
            return memo[i]
        
        return min(helper(0), helper(1))
        