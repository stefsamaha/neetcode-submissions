class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = [] #list of lists
        nums.sort()

        # use each number as a possible first value 
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # not first index but same value as before, we dont want it
                continue 
            
            left, right = i+1, len(nums)-1

            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right-=1
                elif threeSum < 0:
                    left+=1
                else:
                    result.append([a, nums[left], nums[right]])
                    left +=1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
            
        return result

        
        