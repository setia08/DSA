# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

# Example 3:

# Input:
# nums = [1,3,6,10,15], k = 3

# Output:
# 5

# Explanation:
# Subarrays of size 3 are [1,3,6], [3,6,10], and [6,10,15]. 
# Differences are 5, 7, and 9 respectively. 
# The minimum difference is 5 from subarray [1,3,6].


from typing import List
class Solution:
    def minimumDifference(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(nums)-1,0):
            nums[len(nums)-1:len(nums)-3]
        


Sol=Solution()
Sol.minimumDifference()