class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0
        left, right = 0, len(heights)-1
        
        while left < right:
            curr = (right-left)*min(heights[left],heights[right])

            if curr > result:
                result = curr 
            
            if heights[left] < heights[right]:
                left +=1
            else:
                right-=1
        
        return result
                


        