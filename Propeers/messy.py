from typing import List


class Solution:
    def minimumWindowSort(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        start, end = 0, len(nums) - 1

        while start < len(nums) and nums[start] == sorted_nums[start]:
            start += 1

        while end > start and nums[end] == sorted_nums[end]:
            end -= 1

        return end - start + 1 if start < len(nums) else 0


sol = Solution()
print(sol.minimumWindowSort([2, 6, 4, 8, 10, 9, 15]))  # 5
print(sol.minimumWindowSort([1, 2, 3]))                 # 0
print(sol.minimumWindowSort([1, 5, 3, 4, 2, 6]))       # 4