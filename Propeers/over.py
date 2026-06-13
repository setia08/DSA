from typing import List

class Solution:
    def mergeIntervals(self, nums: List[int]) -> List[int]:
        nums.sort()
        output=[nums[0]]
        print(nums)
        for i in range(1,len(nums)):
            if nums[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], nums[i][1])

            # no overlap
            else:
                output.append(nums[i])

        return output
        print(output)


sol=Solution()
sol.mergeIntervals([[1,3],[2,6],[8,10],[15,18]])  # [[1,6],[8,10],[15,18]]