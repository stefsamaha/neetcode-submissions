class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]*len(temperatures)
        stack = [] # pair of (temperature,index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
                
            stack.append((t, i))

        return res 


# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

# Use a monotonic decreasing stack to track days waiting for a warmer temperature.
# Iterate temperatures left → right:

# While current temp is warmer than the stack’s top, pop that index and 
#set res[prev] = current_idx - prev_idx.

# Push current day onto the stack to be resolved later.


# Remaining indices in the stack have no warmer future day → stay 0.
# Each index is pushed and popped at most once → O(n) time, O(n) space.