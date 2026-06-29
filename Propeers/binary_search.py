# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List 
class Solution:
    def searchInsertPosition(self, nums: List[int], target: int) -> int:

        def find_rec(low, high):
            if low > high:
                return low  # FIX 2: insert position, not -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return find_rec(low, mid - 1)
            else:
                return find_rec(mid + 1, high) 

        return find_rec(0, len(nums) - 1)


sol = Solution()
print(sol.searchInsertPosition([1, 3, 5, 6], 5))  # Output: 2