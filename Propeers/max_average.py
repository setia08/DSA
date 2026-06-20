# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List 
class Solution:
    def maximumAverageSubarrayI(self, nums: List[int],k:int) -> List[int]:
        max_avg=float('-inf')
        if k==1:
            return max(nums)
        for i in range(0,len(nums)-k):
            for j in range(i+1,len(nums)):
                if len(nums[i:j])<k:
                   continue
                else:
                   avg=sum(nums[i:j])/len(nums[i:j])
                   if avg>max_avg:
                       max_avg=avg

        return max_avg



sol=Solution()
print(sol.maximumAverageSubarrayI([5],1))