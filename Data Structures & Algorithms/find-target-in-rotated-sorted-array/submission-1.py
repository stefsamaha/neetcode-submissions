class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1 

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid 

            # if left half [l , mid] is sorted 
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # else, right half [mid, r] is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1 


# Key idea

# In a rotated sorted array with unique elements, at least one half (left or right) is sorted in any given step.
# Use that to decide which half could contain the target, and then shrink the search space accordingly.
# Invariants

# We maintain l and r as the current inclusive search window: nums[l..r].
# We compute mid = (l + r) // 2.
# If nums[mid] equals target, we’re done.
# Otherwise, decide which half is sorted and whether the target lies in that sorted half.
# How the two cases work

# Left half is sorted: nums[l] <= nums[mid]

# The sorted range is [nums[l], nums[mid]].
# If target is within that range (nums[l] <= target < nums[mid]), the target must be in the left half, so set r = mid - 1.
# Otherwise, target is not in the left sorted half; it must be in the right half, so set l = mid + 1.
# Right half is sorted: nums[mid] < nums[r]

# The sorted range is [nums[mid], nums[r]].
# If target is within that range (nums[mid] < target <= nums[r]), the target is in the right half, so set l = mid + 1.
# Otherwise, target is not in the right sorted half; it must be in the left half, so set r = mid - 1.
# Why this works

# Because the array was originally sorted and only rotated, one side around mid remains in proper ascending order. If target is in that ascending block, you can safely discard the other half; if not, discard the sorted half and keep the alternative half. Repeating narrows the window logarithmically.
# Concrete walk-through
# Example 1: nums = [4,5,6,7,0,1,2], target = 0

# l=0, r=6, mid=3, nums[mid]=7
# Left half [4,5,6,7] is sorted (nums[l] <= nums[mid]).
# target=0 not in [4,7], so search right half: l = mid + 1 = 4
# Now l=4, r=6, mid=5, nums[mid]=1
# Left half [0,1] is not strictly full, but nums[l] = 0 <= nums[mid] = 1, so left is sorted.
# target=0 is in [0,1], so search left: r = mid - 1 = 4
# l=4, r=4, mid=4, nums[mid]=0 -> found at index 4.
# Example 2: nums = [3,5,6,0,1,2], target = 4

# l=0, r=5, mid=2, nums[mid]=6
# Left half [3,5,6] is sorted.
# target=4 is in [3,6]? 3 <= 4 < 6, yes, so search left: r = mid - 1 = 1
# l=0, r=1, mid=0, nums[mid]=3
# Left half [3] is sorted.
# target=4 not in [3,3], so search right: l = mid + 1 = 1
# l=1, r=1, mid=1, nums[mid]=5
# nums[mid] != target. Left half [5] is sorted.
# target=4 not in [5,5], so search right: l = mid + 1 = 2
# Now l>r, return -1.
# Edge cases to keep in mind

# If the array was rotated by n positions (i.e., effectively not rotated), the algorithm still works because one half remains sorted at each step.
# All elements are unique, so you won’t have equal-at-mid ambiguities.
# The loop ends when l > r, in which case the target isn’t present.
                