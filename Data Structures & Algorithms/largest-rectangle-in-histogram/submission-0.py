class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # O(n) both time and memory 
        maxArea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights):
            start = i # start index of this current height
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index)) # i - index is the width 
                start = index # can extend backwards till index popped 

            stack.append((start,h)) # append start not i, since start is pushed to the max 

        for i, h in stack:
            # get areas of entries not popped
            # not popped means extended till the end, width is len(heights)
            maxArea = max(maxArea, h*(len(heights) - i)) 
            

        return maxArea 




        