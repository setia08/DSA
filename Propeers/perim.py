# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from aiohttp_retry import List

class Solution:
    def largestPerimeterTriangle(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return [nums[i-2], nums[i-1], nums[i]]
        return []