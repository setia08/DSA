# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List
class Solution:
    def longestMountainInArray(self, nums: List[int]) -> List[int]:
        max_length = 0
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                left = i - 1
                right = i + 1
                while left > 0 and nums[left-1] < nums[left]:
                    left -= 1
                while right < len(nums)-1 and nums[right] > nums[right+1]:
                    right += 1
                max_length = max(max_length, right - left + 1)
        return max_length

sol=Solution()
print(sol.longestMountainInArray([2,1,4,7,3,2,5]))  # Output: 5