from typing import List
class Solution:
    def maximumProductOfThreeNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        if len(nums)>=3:
            print(nums[-1],nums[-2],nums[-3])
            product=nums[-1]*nums[-2]*nums[-3]
            return product



Sol=Solution()
Sol.maximumProductOfThreeNumbers([1,2,3])
Sol.maximumProductOfThreeNumbers([-10,-10,5,2])