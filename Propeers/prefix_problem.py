# Input:
# [1,7,3,6,5,6]

# Output:
# 3

# Explanation:
# The pivot index is 3. Left sum = 1 + 7 + 3 = 11, right sum = 5 + 6 = 11.
from typing import List

class Solution:
    def findPivotIndex(self, nums: List[int]) -> List[int]:
        prefix = []
        current = 0
        for num in nums:         
            current += num
            prefix.append(current)

        total = prefix[-1]

        for i in range(0, len(prefix)):
            left_sum  = prefix[i-1] if i > 0 else 0   
            right_sum = total - prefix[i]
            if left_sum == right_sum:
                return i
        return -1
nums=[2,1,-1]
Sol=Solution()
print(Sol.findPivotIndex(nums))