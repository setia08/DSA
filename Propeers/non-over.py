# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
from typing import List
class Solution:
    def nonoverlappingIntervals(self, nums: List[int]) -> List[int]:
        new_arr=[nums[0]]
        counter=0
        for i in range(1,len(nums)):
            if min(nums[i])>=new_arr[-1][1]:
                new_arr.append(nums[i])
            else:
                counter+=1
        print(counter)

Sol=Solution()
Sol.nonoverlappingIntervals([[1,2],[1,2],[1,2]])