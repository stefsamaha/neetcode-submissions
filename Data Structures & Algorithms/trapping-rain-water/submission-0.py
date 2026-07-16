class Solution:
    def trap(self, height: List[int]) -> int:
        # FIRST LINEAR SOLUTION (in memory and time)
        # need to get max left and max right for each entry, and from that we get min(L,R)
        # check if min(L,R) - h[i] >=0 to see how much water can be stored on this level 

        # SECOND LINEAR SOLUTION BUT WITH O(1) MEMORY, MORE EFFICIENT WITH 2 POINTERS
        # 2 pointers, with maxLeft and maxRight, shift smaller value and take min(L,R) to be the smaller value by itself

        if not height: return 0 

        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        result = 0 

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                result += leftMax - height[left]
            else:
                right-=1
                rightMax = max(height[right], rightMax)
                result += rightMax - height[right]

            
        return result 
            



