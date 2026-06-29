# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List
class Solution:
    def maximumProductSubarray(self, nums: List[int]) -> int:
        max_product = float('-inf')
        current_product = 1
        for num in nums:
            current_product *= num
            max_product = max(max_product, current_product)
            if current_product == 0:
                current_product = 1
        return max_product
