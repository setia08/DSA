# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List 
class Solution:
    def maxConsecutiveOnes(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            max_count = 0
            count = 0
            for num in nums:
                if num == 1:
                    count += 1
                    max_count = max(max_count, count)
                else:
                    count = 0
            return max_count

Solution = Solution()   
print(Solution.maxConsecutiveOnes([1,1,0,1,1,1]))  # 3
print(Solution.maxConsecutiveOnes([1,0,1,1,0,1]))  # 2