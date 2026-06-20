# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List
class Solution:
    def subarrayProductLessThanK(self, nums: List[int], k1: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                product = 1
                for k in range(i, j + 1):
                    product *= nums[k]
                if product < k1:
                    result.append(nums[i:j + 1])
        return len(result)

   


sol=Solution()
print(sol.subarrayProductLessThanK([10, 5, 2, 6], 100))  # Output: [[10], [5], [2], [6],