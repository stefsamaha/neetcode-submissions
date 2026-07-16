class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        r, l = 0, 0 
        q = deque() # decreasing deque of values 

        while r < len(nums):
            # maintain decreasing order: drop smaller elements from the back
            while q and q[-1] < nums[r]:
                q.pop()
            
            #add current value
            q.append(nums[r])

            # once we have a full window, record the max and slide 
            if r+1 >= k:
                # front is the max 
                result.append(q[0])

                # if element leaving window is current max, pop it 
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
            r += 1
        
        return result



        