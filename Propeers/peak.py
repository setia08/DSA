from typing import List

class Solution:
    def longestMountainInArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_length = 0
        i = 1

        while i < n - 1:

            if nums[i-1] < nums[i] > nums[i+1]:

                left = i
                right = i

                while left > 0 and nums[left-1] < nums[left]:
                    left -= 1

                while right < n-1 and nums[right] > nums[right+1]:
                    right += 1

                max_length = max(max_length, right - left + 1)

                i = right

            else:
                i += 1

        return max_length


sol=Solution()
print(sol.longestMountainInArray([2, 1, 4, 7, 3, 2, 5]))