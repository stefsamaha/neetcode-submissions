class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        left, right = 0, n-1

        while left < right:
            current = numbers[left]+numbers[right]

            if current > target:
                right -=1
            
            elif current < target:
                left+=1
            
            else:
                return [left+1,right+1]
        
        return []