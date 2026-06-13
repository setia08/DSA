# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

from aiohttp_retry import List


class Solution:
    def squaresOfASortedArray(self, nums: List[int]) -> List[int]:
        nums=[x**2 for x in nums]
        nums.sort()
        return nums