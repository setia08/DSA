# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List
class Solution:
    def maximumPointsYouCanObtainFromCards(self, nums: List[int],Target:List[int]) -> List[int]:
        max=0
        t_sum=0
        j=0
        for i in range(0,len(nums)+1-Target):
            res=sum(nums[i:i+3])
            j+=Target
        max=max if max>res else res
        return max

Solution=Solution()
print(Solution.maximumPointsYouCanObtainFromCards([1,2,3,4,5,6,1], 3) ) # 12