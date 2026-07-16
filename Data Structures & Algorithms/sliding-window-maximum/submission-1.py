class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        window = deque() # double-ended queue, can add and remove elements in O(1) from both ends 

        for i, num in enumerate(nums):

            while window and window[0] < i-k+1:
                window.popleft() # remove entries not belonging to current window 
            
            while window and nums[window[-1]] < num:
                window.pop() # to have max element at the front 
            
            window.append(i) # append current element's index to window

            if i >= k-1: # check if we have reached size k 
                result.append(nums[window[0]]) # if yes, append the first element (max)
            
        return result 
            



        