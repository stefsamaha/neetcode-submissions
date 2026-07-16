class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        left, right = 0, 1 # left is best buy day, right is best sell day 

        while right < len(prices):
            # profitable? 
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, prices[right] - prices[left])

            else:
                left = right # found a min 
            
            right+=1 
        
        return maxProfit 

        
        