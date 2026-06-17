# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List
class Solution:
    def minimumSizeSubarraySum(self, nums: List[int], target: int) -> List[int]:
        min=float('inf')
        for i in range(0,len(nums)+1):
            sub_arr=[]
            counter=0
            total=0
            for j in range(i,len(nums)):

                if total<target:
                    sub_arr.append(nums[j])
                    total+=nums[j]
                    counter+=1

                if total >= target:
                    if counter < min:
                        min = counter
                    break
        return 0 if min == float('inf') else min
