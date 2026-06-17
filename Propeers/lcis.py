from typing import List

class Solution:
    def longestContinuousIncreasingSubsequence(self, nums: List[int]) -> int:
        max_len = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # still increasing
                current += 1
                max_len = max(max_len, current)
            else:
                current = 1  # reset streak

        return max_len


sol = Solution()
print(sol.longestContinuousIncreasingSubsequence([1, 3, 5, 4, 7]))  # 3
print(sol.longestContinuousIncreasingSubsequence([2, 2, 2, 2]))     # 1
print(sol.longestContinuousIncreasingSubsequence([1, 2, 3, 4, 5]))  # 5
